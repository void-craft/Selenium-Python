from selenium.webdriver.common.by import By
from Projects.Project_2.pages.base_page import BasePage

class ProductDetailsPage(BasePage):

    product_name_label = (By.CLASS_NAME, "inventory_details_name.large_size")
    product_price_label = (By.CLASS_NAME, "inventory_details_price")
    add_to_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
    go_back_button = (By.ID, "back-to-products")

    def get_product_name(self):
        return self.driver.find_element(*self.product_name_label).text

    def get_product_price(self):
        return self.driver.find_element(*self.product_price_label).text.strip('$')

    def add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()

    def go_back(self):
        self.driver.find_element(*self.go_back_button).click()
