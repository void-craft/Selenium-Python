from selenium.webdriver.common.by import By
from Projects.Project_3.pages.base_page import BasePage
import random
import string

class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.first_name_field = (By.ID, "firstname")
        self.last_name_field = (By.ID, "lastname")
        self.email_field = (By.ID, "email_address")
        self.password_field = (By.ID, "password")
        self.confirm_password_field = (By.ID, "password-confirmation")
        self.create_account_button = (By.CLASS_NAME, "primary")

    def generate_random_email(self, domain="voidmeow.com"):
        random_string = ''.join(random.choices(string.ascii_lowercase, k=10))
        random_email_address = f"{random_string}@{domain}"
        return random_email_address

    def enter_first_name(self, first_name):
        self.driver.find_element(*self.first_name_field).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(*self.last_name_field).send_keys(last_name)

    def enter_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)
        print()

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element(*self.confirm_password_field).send_keys(confirm_password)

    def click_create_account_button(self):
        self.driver.find_element(*self.create_account_button).click()
