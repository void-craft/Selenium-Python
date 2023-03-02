from selenium.webdriver.common.by import By
from Projects.Project_2.pages.base_page import BasePage

class ProductsPage(BasePage):
    ADD_TO_CART_BUTTON = (
        By.XPATH, "//button[contains(@class,'btn_primary') and contains(text(), 'ADD TO CART')]")
    CART_ICON = (By.XPATH, "//*[@id='shopping_cart_container']/a")

    def add_to_cart(self, product_name):
        product = (By.XPATH,
                   f"//div[contains(@class,'inventory_item_name') and contains(text(),'{product_name}')]/ancestor::div[contains(@class,'inventory_item')]//button[contains(@class,'btn_primary')]")
        self.click(product)

    def go_to_cart(self):
        self.click(self.CART_ICON)

