from selenium.webdriver.common.by import By
from Projects.Project_1.base_page import BasePage
import datetime

class IndiaNewsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.news_feed_locator = (By.CSS_SELECTOR, '.lx-stream__feed')
        self.headlines_locator = (By.CSS_SELECTOR, "h3 a")

    def print_headlines(self):
        headlines_section = self.wait_for_element(self.news_feed_locator)
        headlines = headlines_section.find_elements(*self.headlines_locator)
        now = datetime.datetime.now()
        print("Headlines from India,", now.strftime("%Y-%m-%d %H:%M:%S"))
        for i, headline in enumerate(headlines, 1):
            print(f"{i}. {headline.text}")
