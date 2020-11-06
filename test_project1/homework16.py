import time
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browserstack.local import Local

  # Creates an instance of Local

bs_local = Local()

  # You can also set an environment variable - "BROWSERSTACK_ACCESS_KEY".
bs_local_args = { "key": "hsVngSqitrtGF9LtRCrW" }

  # Starts the Local instance with the required arguments
bs_local.start(**bs_local_args)

  # Check if BrowserStack local instance is running
print(bs_local.isRunning())

  # Stop the Local instance
bs_local.stop()



@pytest.fixture
def driver(request):
    driver = webdriver.Remote(
        command_executor="https://browserstack1654:hsVngSqitrtGF9LtRCrW@hub-cloud.browserstack.com/wd/hub",
        desired_capabilities={"os": "ios", "os_version": "14", "browser": "iphone", "device": "iPhone 11",
                              "real_mobile": True, "browserstack.local": True})
    request.addfinalizer(driver.quit)
    return driver


def test_create_site_form(driver):
    driver.get("http://kzhukova.app.alpha-web.resto.lan/")
    time.sleep(10)
    driver.find_element_by_name("login").send_keys('admin')
    driver.find_element_by_name("password").send_keys('resto#test')
    driver.find_element_by_css_selector("button").click()
    driver.get("http://kzhukova.app.alpha-web.resto.lan/site-constructor/ru-RU/index.html#/sites")
    driver.find_element_by_css_selector("div.d-flex.align-items-center.fx-mobile > button").click()
    create_box = driver.find_element_by_tag_name("iiko-create-site")
    # проверка домена
    domen_mask = 'AT' + str(datetime.now().date()) + str(datetime.now().hour) + str(datetime.now().minute) + str(datetime.now().second)
    domen = WebDriverWait(create_box, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mat-input-1')))
    domen.send_keys("kzhu" + Keys.ENTER)
    if create_box.find_element_by_id("mat-error-0").get_attribute('textContent') != "Не менее 6 символов" or create_box.find_element_by_css_selector("div > div > button.mat-focus-indicator.mat-raised-button.mat-button-base.mat-primary").get_attribute("disabled") != 'true':
        raise Exception()
    domen.send_keys("kova5" + Keys.ENTER)
    if create_box.find_element_by_id("mat-error-0").get_attribute('textContent') != "Уже существует" or create_box.find_element_by_css_selector("div > div > button.mat-focus-indicator.mat-raised-button.mat-button-base.mat-primary").get_attribute("disabled") != 'true':
        raise Exception()
    domen.send_keys(Keys.CONTROL+ "a"+ Keys.BACKSPACE)
    domen.send_keys(domen_mask)
    time.sleep(3)
    if create_box.find_element_by_css_selector(
            "div > div > button.mat-focus-indicator.mat-raised-button.mat-button-base.mat-primary").get_attribute(
            "disabled"):
        raise Exception()
    # проверить, что выбрано QR
    if create_box.find_element_by_css_selector("#mat-radio-2-input").get_attribute("checked") != 'true':
        raise Exception()
    # выбрать меню
    create_box.find_element_by_css_selector("div.mat-form-field-infix.ng-tns-c72-10").click()
    listOfMenu = driver.find_element_by_id('mat-select-0-panel')
    time.sleep(1)
    menus = listOfMenu.find_elements_by_css_selector("span.mat-option-text")
    for menu in menus:
        if menu.get_attribute('textContent') == 'базовый':
            menu.click()
            break
    # создать меню
    create_box.find_element_by_css_selector("div > div > button.mat-focus-indicator.mat-raised-button.mat-button-base.mat-primary").click()
    driver.find_element_by_xpath("//*[contains(text(), 'Удалить сайт')]").click()
    driver.find_element_by_css_selector(
        'iiko-confirm-dialog button.mat-focus-indicator.mat-raised-button.mat-button-base.mat-primary').click()
    time.sleep(2)


