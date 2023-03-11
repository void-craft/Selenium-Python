from selenium.webdriver.common.by import By
from Projects.Project_2.pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = "https://www.saucedemo.com/"
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def enter_username(self):
        self.input_text(self.username_input, "standard_user")

    def enter_password(self):
        self.input_text(self.password_input, "secret_sauce")

    def click_login(self):
        self.click_element(self.login_button)

    def go_to(self):
        self.driver.get(self.url)
