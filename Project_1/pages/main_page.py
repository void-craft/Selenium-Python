from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
    def load_page(self, url):
        self.driver.get(url)
    def reject_cookies(self):
        reject_button = self.wait.until(ec.presence_of_element_located((By.XPATH, "//*[@aria-label='Do not consent']")))
        reject_button.click()
    def go_to_news_page(self):
        news_tab = self.wait.until(ec.presence_of_element_located((By.XPATH, "//a[text()='News']")))
        news_tab.click()