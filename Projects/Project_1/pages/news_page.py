from selenium.webdriver.common.by import By
from Projects.Project_1.base_page import BasePage

class NewsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.world_news_locator = (By.LINK_TEXT, "World")
        self.asia_news_locator = (By.LINK_TEXT, "Asia")
        self.india_news_locator = (By.LINK_TEXT, "India")

    def click_world_news_link(self):
        self.click_element(self.world_news_locator)

    def click_asia_news_link(self):
        self.click_element(self.asia_news_locator)

    def click_india_news_link(self):
        self.click_element(self.india_news_locator)
