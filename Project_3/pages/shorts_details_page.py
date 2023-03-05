import time

from selenium.webdriver.common.by import By
from Projects.Project_3.pages.base_page import BasePage


class ShortsDetailsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.shorts_size = (By.ID, "option-label-size-143-item-177")
        self.shorts_color = (By.ID, "option-label-color-93-item-49")
        self.shorts_quantity = (By.ID, "qty")
        self.shorts_add_to_cart = (By.ID, "product-addtocart-button")
        self.show_cart = (By.CLASS_NAME, "minicart-wrapper")
        self.checkout = (By.ID, "top-cart-btn-checkout")
        self.quantity_text = "2"

    def add_shorts_to_cart(self):
        shorts_size = self.wait_for_element(self.shorts_size)
        shorts_size.click()
        shorts_color = self.wait_for_element(self.shorts_color)
        shorts_color.click()
        shorts_quantity = self.wait_for_element(self.shorts_quantity)
        shorts_quantity.clear()
        shorts_quantity.send_keys(self.quantity_text)
        shorts_add_to_cart = self.wait_for_element(self.shorts_add_to_cart)
        shorts_add_to_cart.click()
        time.sleep(3)

    def open_cart(self):
        show_cart = self.wait_for_element(self.show_cart)
        show_cart.click()
        checkout = self.wait_for_element(self.checkout)
        checkout.click()


