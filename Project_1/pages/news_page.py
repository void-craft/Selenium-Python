from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
class NewsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
    def go_to_world_news_page(self):
        world_link = self.wait.until(ec.presence_of_element_located((By.LINK_TEXT, "World")))
        world_link.click()
    def go_to_asia_news_page(self):
        asia_link = self.wait.until(ec.presence_of_element_located((By.LINK_TEXT, "Asia")))
        asia_link.click()
    def go_to_india_news_page(self):
        india_link = self.wait.until(ec.presence_of_element_located((By.LINK_TEXT, "India")))
        india_link.click()