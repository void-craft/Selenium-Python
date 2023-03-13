from selenium.webdriver.common.by import By
from Project_3.pages.base_page import BasePage

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.open_website = "https://magento.softwaretestingboard.com"
        self.create_account_link = (By.LINK_TEXT, "Create an Account")

    def open_magneto_website(self):
        self.driver.get(self.open_website)

    def create_account(self):
        self.click_element(self.create_account_link)








