from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 10)

    def wait_for_element(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element

    def click_element(self, by_locator):
        element = self.wait_for_element(by_locator).click()
        return element

    def send_keys_to_element(self, by_locator, text):
        element = self.wait_for_element(by_locator)
        element.clear()
        element.send_keys(text)

    def hover(self, by_locator):
        element = self.wait_for_element(by_locator)
        self.action.move_to_element(element).perform()

    def select_dropdown_option(self, by_locator, option):
        select_element = Select(self.wait_for_element(by_locator))
        select_element.select_by_visible_text(option)
