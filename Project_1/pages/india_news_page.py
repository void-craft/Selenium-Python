from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import datetime
class IndiaNewsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
    def get_headlines(self):
        headlines_section = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '.lx-stream__feed')))
        headlines = headlines_section.find_elements(By.CSS_SELECTOR, "h3 a")
        now = datetime.datetime.now()
        print("Headlines from India,", now.strftime("%Y-%m-%d %H:%M:%S"))
        for i, headline in enumerate(headlines, 1):
            print(f"{i}. {headline.text}")
