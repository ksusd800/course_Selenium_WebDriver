import time

import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(1)
    request.addfinalizer(wd.quit)
    return wd


# def is_element_present(driver, *args):
#     try:
#         driver.find_element(*args)
#         return True
#     except NoSuchElementException:
#         return False


def login(driver):
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').click()


def test_click(driver):
    driver.get("http://localhost:8080/litecart/admin/")
    login(driver)
    #is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_tag_name('h1')
    menu = driver.find_element_by_id('box-apps-menu-wrapper')
    items = menu.find_elements_by_css_selector('#app- > a')
    len_items = len(items)
    time.sleep(1)
    for i in range(0, len_items):
        menu = driver.find_element_by_id('box-apps-menu-wrapper')
        items = menu.find_elements_by_css_selector('#app- > a')
        items[i].click()
        #is_element_present(driver, By.TAG_NAME, "h1")
        driver.find_element_by_tag_name('h1')
        # вложенные пункты:
        menu = driver.find_element_by_id('box-apps-menu-wrapper')
        items_inside = menu.find_elements_by_css_selector('ul.docs > li')
        len_items_inside = len(items_inside)
        if len_items_inside > 0:
            for k in range(len_items_inside):
                menu = driver.find_element_by_id('box-apps-menu-wrapper')
                items_inside = menu.find_elements_by_css_selector('ul.docs > li')
                items_inside[k].click()
                # is_element_present(driver, By.TAG_NAME, "h1")
                driver.find_element_by_tag_name('h1')
