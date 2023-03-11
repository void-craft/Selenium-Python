import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def wait_for_element(self, locator):
        element = self.wait.until(ec.visibility_of_element_located(locator))
        return element

    def click_element(self, by_locator):
        element = self.wait_for_element(by_locator).click()
        return element

    def add_text(self, by_locator, text):
        element = self.wait_for_element(by_locator)
        element.clear()
        element.send_keys(text)

    def go_back(self):
        self.driver.back()

    def maximize_window(self):
        self.driver.maximize_window()

    def sleep_for_5_seconds(self):
        time.sleep(5)