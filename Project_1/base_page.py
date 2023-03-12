import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 10)

    def open_website(self, url):
        self.driver.get(url)

    def wait_for_element(self, locator):
        element = self.wait.until(ec.visibility_of_element_located(locator))
        return element

    def click_element(self, by_locator):
        element = self.wait_for_element(by_locator).click()
        return element

    def send_keys_to_element(self, by_locator, text):
        element = self.wait_for_element(by_locator)
        element.clear()
        element.send_keys(text)

    def select_option_from_dropdown(self, by_locator, text):
        element = self.wait_for_element(by_locator)
        element.send_keys(text)

    def hover(self, by_locator):
        element = self.wait_for_element(by_locator)
        self.action.move_to_element(element).perform()

    def select_dropdown_option(self, by_locator, option):
        select_element = Select(self.wait_for_element(by_locator))
        select_element.select_by_visible_text(option)

    def go_back(self):
        self.driver.back()

    def maximize_window(self):
        self.driver.maximize_window()


    def sleep_for_5_seconds(self):
        time.sleep(5)