import time
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(5)
    request.addfinalizer(wd.quit)
    return wd


def test_new_user(driver):
    driver.get("http://localhost:8080/litecart")
    driver.find_element_by_css_selector('#box-account-login  a').click()
    time.sleep(1)
    driver.find_element_by_css_selector('[name = firstname]').send_keys('MyFirstname')
    driver.find_element_by_css_selector('[name = lastname]').send_keys('MyLastname')
    driver.find_element_by_css_selector('[name = address1]').send_keys('Myaddress1')
    driver.find_element_by_css_selector('[name = postcode]').send_keys('01234')
    driver.find_element_by_css_selector('[name = city]').send_keys('Chicago')
    Select(driver.find_element_by_css_selector('[name = country_code]')).select_by_value('US')
    sel = driver.find_elements_by_css_selector('#create-account select')
    zones = sel[1]
    Select(zones).select_by_value('IL')
    mask = 'testmail_' + str(datetime.now().date()) + '_' + str(datetime.now().hour) + str(datetime.now().minute) + str(datetime.now().second) + '@test.ru'
    driver.find_element_by_css_selector('[name = email]').send_keys(mask)
    driver.find_element_by_css_selector('[name = phone]').send_keys('+19399999999')
    driver.find_element_by_css_selector('[name = password]').send_keys('Test000!')
    driver.find_element_by_css_selector('[name = confirmed_password]').send_keys('Test000!')
    driver.find_element_by_css_selector('[name = create_account]').click()
    driver.find_element_by_link_text('Logout').click()
    driver.find_element_by_css_selector('[name = email]').send_keys(mask)
    driver.find_element_by_css_selector('[name = password]').send_keys('Test000!')
    driver.find_element_by_css_selector('[name = login]').click()
    driver.find_element_by_link_text('Logout').click()
