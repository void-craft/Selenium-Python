from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def wait_for_element(self, locator):
        element = self.wait.until(ec.visibility_of_element_located(locator))
        return element

    def navigate_to_url(self, url):
        self.driver.get(url)

    def click_element(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    def input_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def maximize_window(self):
        self.driver.maximize_window()


