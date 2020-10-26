import pytest
from selenium import webdriver
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    #wd = webdriver.Firefox()
    #wd = webdriver.Ie()
    wd.implicitly_wait(5)
    request.addfinalizer(wd.quit)
    return wd


def test_cart(driver):
    i = 0
    driver.get("http://localhost:8080/litecart")
    # добавление в корзину 3 товара
    while i < 3:
        driver.find_element_by_class_name("product").click()
        # если есть выбор опции
        opt = driver.find_elements_by_name("options[Size]")
        if len(opt) > 0:
            Select(driver.find_element_by_name('options[Size]')).select_by_index('1')
            time.sleep(2)
        quan1 = int(driver.find_element_by_css_selector("#cart span.quantity").get_attribute('textContent'))+1
        driver.find_element_by_css_selector("[name = add_cart_product]").click()
        # подождать обновление счетчика
        wait = WebDriverWait(driver, 10)  # seconds
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#cart span.quantity"), str(quan1)))
        driver.back()
        i += 1
    # удаление из корзины:
    driver.find_element_by_css_selector("#cart > a.link").click()
    rows = driver.find_elements_by_css_selector("#order_confirmation-wrapper td.item")
    while len(rows) > 1:
        products1 = driver.find_elements_by_tag_name("#box-checkout-cart > ul > li")
        len_prod = len(products1)
        while len_prod > 1:
            boxprod = driver.find_element_by_css_selector("#box-checkout-cart > ul")
            products1 = boxprod.find_elements_by_tag_name("li")
            products1[0].click()
            nametable = driver.find_element_by_css_selector("#order_confirmation-wrapper > table > tbody > tr:nth-child(2)")
            driver.find_element_by_css_selector("[name=remove_cart_item]").click()
            # ждем пока в таблице пропадет товар
            wait = WebDriverWait(driver, 10)  # seconds
            wait.until(EC.staleness_of(nametable))
            len_prod -= 1
        rows = driver.find_elements_by_css_selector("#order_confirmation-wrapper td.item")
    driver.find_element_by_css_selector("[name=remove_cart_item]").click()




