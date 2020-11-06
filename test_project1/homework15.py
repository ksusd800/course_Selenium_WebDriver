import time
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select


@pytest.fixture
def driver(request):
    driver = webdriver.Remote("http://192.168.52.1:4444/wd/hub", desired_capabilities={"browserName": "chrome", "platform": "WINDOWS"})
    request.addfinalizer(driver.quit)
    return driver


def test_new_user(driver):
    #driver.get("http://localhost:8080/litecart")
    #driver = webdriver.Remote("http://192.168.52.1:4444/wd/hub", desired_capabilities={"browserName": "internet explorer"})
    driver.get("http://www.ya.ru")
   # driver.get("http://localhost:8080/litecar/admin")
    #driver.find_element_by_name('username').send_keys('admin')
   # driver.find_element_by_name('password').send_keys('admin')
   # driver.find_element_by_name('login').click()