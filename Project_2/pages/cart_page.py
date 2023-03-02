from selenium.webdriver.common.by import By
from Projects.Project_2.pages.base_page import BasePage

class CartPage(BasePage):
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        super().__init__(driver)

    CHECKOUT_BUTTON = (By.NAME, "checkout")

    def open_cart(self):
        self.click(self.CART_ICON)

    def checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    def calculate_subtotal(self):
        subtotal = 0
        items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        for item in items:
            price = float(item.find_element(By.CLASS_NAME, "inventory_item_price").text[1:])
            quantity = int(item.find_element(By.CLASS_NAME, "cart_quantity").text)
            subtotal += price * quantity
        return round(subtotal, 2)
