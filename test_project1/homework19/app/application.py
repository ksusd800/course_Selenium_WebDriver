from selenium import webdriver
from homework19.pages.main_page import MainPage
from homework19.pages.product_page import ProductPage
from homework19.pages.cart_page import CartPage


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.main_page = MainPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.cart_page = CartPage(self.driver)

    def quit(self):
        self.driver.quit()

    def count_items_in_cart(self):
        self.main_page.open()
        return self.main_page.count_product_in_cart()

    def add_product_in_cart(self):
        self.main_page.open()
        # добавление в корзину n товара
        i = 0
        while i < 3:
            self.main_page.open_product()
            self.product_page.check_option_size()
            quan_old = self.product_page.count_product_in_cart()
            self.product_page.add_in_cart_button().click()
            self.product_page.wait_update_count_in_cart(quan_old)
            self.driver.back()
            i += 1

    def delete_product_from_cart(self):
        self.cart_page.open()
        len_rows = self.cart_page.count_product_in_table()
        while len_rows > 1:
            len_prod = self.cart_page.count_product_with_icons()
            while len_prod > 1:
                self.cart_page.click_on_first_in_list()
                nametable = self.cart_page.get_the_first_item_in_table()
                self.cart_page.button_delete_product()
                self.cart_page.wait_update_count_in_cart(nametable)
                len_prod -= 1
            len_rows = self.cart_page.count_product_in_table()
        self.cart_page.button_delete_product()







