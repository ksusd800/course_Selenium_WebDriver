from selenium.webdriver.support.wait import WebDriverWait


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("http://localhost:8080/litecart/")
        return self

    #открыть продукт
    def open_product(self):
        self.driver.find_element_by_class_name("product").click()
        return self

    def count_product_in_cart(self):
        return self.driver.find_element_by_css_selector("#cart span.quantity").get_attribute('textContent')

