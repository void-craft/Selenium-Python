from selenium.webdriver.common.by import By
from Projects.

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.open_website = "https://www.google.com"
        self.reject_cookie_locator = (By.ID, "W0wltc")

