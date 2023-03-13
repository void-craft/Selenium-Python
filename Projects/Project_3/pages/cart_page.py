import time

from selenium.webdriver.common.by import By
from Project_3.pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.address = (By.XPATH, '//*[@id="NR4OVVY"]')
        self.address_text = "Dark dark place"
        self.city = (By.XPATH, '/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form/div/div[4]/div/input')
        self.city_text = "Dark city"
        self.phone = (By.XPATH, '/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form/div/div[9]/div/input')
        self.phone_text = "987654321"
        self.country = (By.XPATH, '/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form/div/div[8]/div/select')
        self.country_text = "sp"
        self.province = (By.XPATH, '/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form/div/div[5]/div/select')
        self.province_text = "as"
        self.zipcode = (By.XPATH, '/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form/div/div[7]/div/input')
        self.zipcode_text = "33333"
        self.next_button = (By.XPATH, '/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[2]/div/div[3]/form/div[3]/div/button/span')
        self.billing_address = (By.ID, "billing-address-same-as-shipping-checkmo")
        self.place_order_button = (By.XPATH, '/html/body/div[3]/main/div[2]/div/div[2]/div[4]/ol/li[3]/div/form/fieldset/div[1]/div/div/div[2]/div[2]/div[4]/div/button')
        self.order_number = (By.CLASS_NAME, "order-number")

    def place_order(self):
        self.send_keys_to_element(self.address)
        self.send_keys_to_element(self.city)
        self.send_keys_to_element(self.phone)
        self.send_keys_to_element(self.country)
        self.select_option_from_dropdown(self.province)
        self.send_keys_to_element(self.zipcode)
        self.sleep_for_5_seconds()
        self.click_element(self.next_button)
        self.click_element(self.place_order_button)

    def get_order_number(self):
        order_number = self.wait_for_element(self.order_number)
        order_number_text = str(order_number.text)
        print(f"Your order number is: {order_number_text}")
        return order_number_text



