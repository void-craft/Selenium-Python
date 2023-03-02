from selenium.webdriver.common.by import By
from Projects.Project_2.pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

    URL = "https://www.saucedemo.com/"

    username_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_button = (By.ID, "login-button")

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        self.go_to()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def go_to(self):
        self.driver.get(self.URL)
