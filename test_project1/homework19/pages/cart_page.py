from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("http://localhost:8080/litecart/en/checkout")
        return self

    def count_product_in_table(self):
        return len(self.driver.find_elements_by_css_selector("#order_confirmation-wrapper td.item"))

    def count_product_with_icons(self):
        products = self.driver.find_elements_by_tag_name("#box-checkout-cart > ul > li")
        len_list = len(products)
        return len_list

    def click_on_first_in_list(self):
        list_prod = self.driver.find_elements_by_tag_name("#box-checkout-cart > ul > li")
        list_prod[0].click()
        return self

    def get_the_first_item_in_table(self):
        nametable = self.driver.find_element_by_css_selector(
            "#order_confirmation-wrapper > table > tbody > tr:nth-child(2)")
        return nametable

    def button_delete_product(self):
        self.driver.find_element_by_css_selector("[name=remove_cart_item]").click()
        return self

    def wait_update_count_in_cart(self, nametable):
        WebDriverWait(self.driver, 10).until(EC.staleness_of(nametable))

