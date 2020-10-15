import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd_ff1 = webdriver.Firefox()
   # старая версия:
   # wd_ff = webdriver.Firefox(capabilities={"marionette": False})
    wd_ff1 = webdriver.Firefox(firefox_binary="c:\\Program Files\\Firefox Nightly\\firefox.exe")
    request.addfinalizer(wd_ff1.quit)
    return wd_ff1


def test_example(driver):
    driver.get("http://localhost:8080/litecart/admin/")
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').click()


