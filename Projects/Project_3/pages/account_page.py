from selenium.webdriver.common.by import By
from Project_3.pages.base_page import BasePage

class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.first_name_field = (By.ID, "firstname")
        self.last_name_field = (By.ID, "lastname")
        self.email_field = (By.ID, "email_address")
        self.password_field = (By.ID, "password")
        self.confirm_password_field = (By.ID, "password-confirmation")
        self.create_account_button = (By.CLASS_NAME, "primary")
        self.hoodies_link = (By.ID, "ui-id-12")
        self.women_dropdown = (By.LINK_TEXT, "Women")
        self.top_expansion = (By.ID, "ui-id-9")

    def enter_first_name(self):
        self.send_keys_to_element(self.first_name_field, "Void")

    def enter_last_name(self):
        self.send_keys_to_element(self.last_name_field, "Craft")

    def enter_email(self):
        email = self.generate_random_email('voidcraft')
        self.send_keys_to_element(self.email_field, email)

    def enter_password(self):
        password = self.generate_random_password()
        self.send_keys_to_element(self.password_field, password)
        self.send_keys_to_element(self.confirm_password_field, password)

    def click_create_account_button(self):
        self.click_element(self.create_account_button)

    def navigate_to_hoodies(self):
        self.hover(self.women_dropdown)
        self.hover(self.top_expansion)
        self.click_element(self.hoodies_link)

