from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

   # def open(self):
   #     self.driver.get("http://localhost:8080/litecart/")
   #     return self

    def check_option_size(self):
        if len(self.driver.find_elements_by_name("options[Size]")) > 0:
            Select(self.driver.find_element_by_name('options[Size]')).select_by_index('1')

    def count_product_in_cart(self):
        quan_old = int(self.driver.find_element_by_css_selector("#cart span.quantity").get_attribute('textContent'))
        return quan_old

    def add_in_cart_button(self):
        return self.driver.find_element_by_css_selector("[name = add_cart_product]")

    def wait_update_count_in_cart(self, quan_old):
        quan_new = quan_old + 1
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#cart span.quantity"), str(quan_new)))