import os
from datetime import datetime
import time

from selenium.webdriver.common.keys import Keys
import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select


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


def test_add_product(driver):
    login(driver)
    driver.get("http://localhost:8080/litecart/admin/?app=catalog&doc=catalog")
    driver.find_element_by_css_selector('#content > div:nth-child(2) > a:nth-child(2)').click()
    time.sleep(1)
    # general
    wind = driver.find_element_by_css_selector('#tab-general')
    wind.find_element_by_css_selector('tr:nth-child(1) input[value = "1"]').click()
    mask = 'test Duck' + str(datetime.now())
    wind.find_element_by_css_selector('[name = "name[en]"]').send_keys(mask)
    wind.find_element_by_css_selector('[name = code]').send_keys('001')
    wind.find_element_by_css_selector('tr:nth-child(4) input[data-name = "Root"]').click()
    wind.find_element_by_css_selector('tr:nth-child(4) input[data-name = "Rubber Ducks"]').click()
    wind.find_element_by_css_selector('tr:nth-child(4) input[data-name = "Subcategory"]').click()
    Select(driver.find_element_by_css_selector('[name = default_category_id]')).select_by_value('2')
    wind.find_element_by_css_selector('tr:nth-child(7) input[value = "1-2"]').click()
    wind.find_element_by_css_selector('tr:nth-child(7) input[value = "1-1"]').click()
    wind.find_element_by_css_selector('tr:nth-child(8) input[name = "quantity"]').send_keys(Keys.HOME + '1' + Keys.RIGHT + Keys.BACKSPACE)
    wind.find_element_by_css_selector('tr:nth-child(10) input[name = "date_valid_from"]').send_keys('01102020')
    wind.find_element_by_css_selector('tr:nth-child(11) input[name = "date_valid_to"]').send_keys('31122020')
    path_image = os.getcwd() + '\duck.jpg'
    wind.find_element_by_css_selector('tr:nth-child(9) input[name = "new_images[]"]').send_keys(path_image)
    # information
    time.sleep(1)
    driver.find_element_by_css_selector('.index a[href="#tab-information"]').click()
    Select(driver.find_element_by_css_selector('[name = manufacturer_id]')).select_by_value('1')
    driver.find_element_by_css_selector('[name = "keywords"]').send_keys('my_keywords')
    driver.find_element_by_css_selector('[name = "short_description[en]"]').send_keys('My_short_description')
    driver.find_element_by_css_selector('div.trumbowyg-editor').send_keys('My_description')
    driver.find_element_by_css_selector('[name = "head_title[en]"]').send_keys('My_head_title')
    driver.find_element_by_css_selector('[name = "meta_description[en]"]').send_keys('My_meta_description')
    # prices
    time.sleep(1)
    driver.find_element_by_css_selector('.index a[href="#tab-prices"]').click()
    driver.find_element_by_css_selector('[name = "purchase_price"]').send_keys(Keys.HOME + '2' )
    Select(driver.find_element_by_css_selector('[name = purchase_price_currency_code]')).select_by_value('USD')
    driver.find_element_by_css_selector('[name = "prices[USD]"]').send_keys(Keys.HOME + '20' )
    driver.find_element_by_css_selector('[name = "prices[EUR]"]').send_keys(Keys.HOME + '19')
    # save and find
    driver.find_element_by_css_selector('[name = "save"]').click()
    driver.find_element_by_link_text('Rubber Ducks').click()
    driver.find_element_by_link_text('Subcategory').click()
    listofproduct = driver.find_element_by_class_name('dataTable')
    listofproduct.find_element_by_link_text(mask)



