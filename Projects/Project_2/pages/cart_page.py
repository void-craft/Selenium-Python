from selenium.webdriver.common.by import By
from Project_2.pages.base_page import BasePage
class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")
        self.checkout_button = (By.NAME, "checkout")
        self.cart_item = (By.CLASS_NAME, "cart_item")
        self.inventory_item1_price = (By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
        self.inventory_item2_price = (By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[4]/div[2]/div[2]/div')
        self.cart_quantity = (By.CLASS_NAME, "cart_quantity")

    def open_cart(self):
        self.click_element(self.cart_icon)

    def click_checkout(self):
        self.click_element(self.checkout_button)

    def calculate_subtotal(self):
        item1_price = float(self.wait_for_element(self.inventory_item1_price).text.replace('$', ''))
        item2_price = float(self.wait_for_element(self.inventory_item2_price).text.replace('$', ''))
        subtotal = item1_price + item2_price
        return float(subtotal)

