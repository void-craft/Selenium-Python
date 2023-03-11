from selenium.webdriver.common.by import By
from Project_1.base_page import BasePage

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.bbc.com"
        self.reject_cookies_locator = (By.XPATH, "//*[@aria-label='Do not consent']")
        self.news_tab_locator = (By.XPATH, "//a[text()='News']")

    def open_website(self):
        self.driver.get(self.url)

    def go_full_screen(self):
        self.maximize_window()

    def reject_cookies(self):
        self.click_element(self.reject_cookies_locator)

    def click_news_tab(self):
        self.click_element(self.news_tab_locator)
