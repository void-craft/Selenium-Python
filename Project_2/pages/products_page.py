from selenium.webdriver.common.by import By
from Projects.Project_2.pages.base_page import BasePage
class ProductsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.add_to_cart_button = (By.XPATH, "//button[contains(@class,'btn_primary') and contains(text(), 'ADD TO CART')]")
        self.cart_icon = (By.XPATH, "//*[@id='shopping_cart_container']/a")
        self.product1 = (By.XPATH, f"//div[contains(@class,'inventory_item_name') and contains(text(), 'Sauce Labs Bike Light')]/ancestor::div[contains(@class,'inventory_item')]//button[contains(@class,'btn_primary')]")
        self.product2 = (By.XPATH, f"//div[contains(@class,'inventory_item_name') and contains(text(), 'Sauce Labs Backpack')]/ancestor::div[contains(@class,'inventory_item')]//button[contains(@class,'btn_primary')]")

    def add_products_to_cart(self):
        self.click_element(self.product1)
        self.click_element(self.product2)

    def go_to_cart(self):
        self.click_element(self.cart_icon)
