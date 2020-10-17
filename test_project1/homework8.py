import time

import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(5)
    request.addfinalizer(wd.quit)
    return wd


def test_stick(driver):
    driver.get("http://localhost:8080/litecart")
    products = driver.find_elements_by_class_name('product')
    for item in products:
        stickers = item.find_elements_by_css_selector("[class ^= sticker]")
        if len(stickers) != 1:
            raise Exception()