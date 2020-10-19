import time

import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(1)
    request.addfinalizer(wd.quit)
    return wd


def login(driver):
    driver.get("http://localhost:8080/litecart/admin/")
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').click()

# часть 1 (http://localhost/litecart/admin/?app=countries&doc=countries):
def test_Countries(driver):
    login(driver)
    driver.get("http://localhost:8080/litecart/admin/?app=countries&doc=countries")
    table_countries = driver.find_element_by_css_selector('#content > form')
    rows = table_countries.find_elements_by_class_name('row')
    listcountries_base = []
    countries_with_zones = []
    for row in rows:
        country = row.find_element_by_css_selector('td:nth-child(5) > a')
        # вычисляем те страны, у кого есть зоны:
        if row.find_element_by_css_selector('td:nth-child(6)').text != '0':
            country_link = country.get_attribute("href")
            countries_with_zones.append(country_link)
        listcountries_base.append(country.text)
    listcountries_sorted = sorted(listcountries_base)
    # если оригинальный список стран и отсортированный отличаются, значит страны на странице не отсортированы
    if listcountries_base != listcountries_sorted:
        raise Exception()
    # проходим по странам, у которых есть зоны и проверяем сортировку зон:
    for i in countries_with_zones:
        zones = []
        driver.get(i)
        table_zones = driver.find_element_by_css_selector('#table-zones')
        rows_zone = table_zones.find_elements_by_css_selector('td:nth-child(3) > input[type=hidden]')
        for row in rows_zone:
            zones.append(row.get_attribute('value'))
        zones_sorted = sorted(zones)
        if zones_sorted != zones:
            raise Exception()


# часть 2 (http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones):
def test_zones(driver):
    login(driver)
    driver.get("http://localhost:8080/litecart/admin/?app=geo_zones&doc=geo_zones")
    table_countries = driver.find_element_by_css_selector('#content > form')
    rows = table_countries.find_elements_by_class_name('row')
    countries_with_zones = []
    # собираем ссылки на страны:
    for row in rows:
        country = row.find_element_by_css_selector('td:nth-child(3) > a')
        countries_with_zones.append(country.get_attribute("href"))
    # проходим по каждой стране из списка
    for i in countries_with_zones:
        zones = []
        driver.get(i)
        table_zones = driver.find_element_by_css_selector('#table-zones')
        rows_zone = table_zones.find_elements_by_css_selector('td:nth-child(3) > select')
        # находим в таблице зон выбранный в списке зон элемент по каждой строке
        for row in rows_zone:
            options = row.find_elements_by_tag_name('option')
            for i in options:
                if i.is_selected():
                    zones.append(i.text)
        # сравниваем сортированный список и оригинальный
        zones_sorted = sorted(zones)
        if zones_sorted != zones:
            raise Exception()