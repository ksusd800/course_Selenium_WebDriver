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


def test_logs(driver):
    login(driver)
    driver.get("http://localhost:8080/litecart/admin/?app=catalog&doc=catalog&category_id=2")
    listofproduct = driver.find_element_by_class_name('dataTable')
    products = listofproduct.find_elements_by_css_selector('td:nth-child(3) > a[href^="http://localhost:8080/litecart/admin/?app=catalog&doc=edit_product"]')
    print(len(products))
    x = len(products)
    for i in range(x):
        listofproduct = driver.find_element_by_class_name('dataTable')
        products = listofproduct.find_elements_by_css_selector(
            'td:nth-child(3) > a[href^="http://localhost:8080/litecart/admin/?app=catalog&doc=edit_product"]')
        products[i].click()
        if len(driver.get_log("browser")) > 0:
            raise Exception()
        driver.back()
