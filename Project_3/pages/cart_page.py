import time

from selenium.webdriver.common.by import By
from Projects.Project_3.pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.address = (By.XPATH, '/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form/div/fieldset/div/div[1]/div/input')
        self.address_text = "Dark, dark place"
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
        address = self.wait_for_element(self.address)
        address.clear()
        address.send_keys(self.address_text)
        city = self.wait_for_element(self.city)
        city.clear()
        city.send_keys(self.city_text)
        phone = self.wait_for_element(self.phone)
        phone.clear()
        phone.send_keys(self.phone_text)
        country = self.wait_for_element(self.country)
        country.send_keys(self.country_text)
        province = self.wait_for_element(self.province)
        province.send_keys(self.province_text)
        zipcode = self.wait_for_element(self.zipcode)
        zipcode.clear()
        zipcode.send_keys(self.zipcode_text)
        time.sleep(5)
        next_button = self.wait_for_element(self.next_button)
        next_button.click()
        #billing_address = self.wait_for_element(self.billing_address)
       # billing_address.click()
        place_order_button = self.wait_for_element(self.place_order_button)
        place_order_button.click()

    def get_order_number(self):
        order_number = self.wait_for_element(self.order_number)
        order_number_text = str(order_number.text)
        print(f"Your order number is: {order_number_text}")
        return order_number_text



