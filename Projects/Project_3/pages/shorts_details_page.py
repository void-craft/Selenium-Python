import time

from selenium.webdriver.common.by import By
from Project_3.pages.base_page import BasePage


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
        self.click_element(self.shorts_size)
        self.click_element(self.shorts_color)
        self.send_keys_to_element(self.shorts_quantity, self.quantity_text)
        self.click_element(self.shorts_add_to_cart)

    def open_cart(self):
        self.click_element(self.show_cart)
        self.click_element(self.checkout)


