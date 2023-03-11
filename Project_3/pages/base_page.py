import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import random
import string


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

    def select_option_from_dropdown(self, by_locator, text):
        element = self.wait_for_element(by_locator)
        element.send_keys(text)

    def hover(self, by_locator):
        element = self.wait_for_element(by_locator)
        self.action.move_to_element(element).perform()

    def select_dropdown_option(self, by_locator, option):
        select_element = Select(self.wait_for_element(by_locator))
        select_element.select_by_visible_text(option)

    def generate_random_email(self, domain):
        random_string = ''.join(random.choices(string.ascii_lowercase, k=10))
        random_email_address = f"{random_string}@{domain}"
        return random_email_address
    def generate_random_password(self, length=10):
        password_chars = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choices(password_chars, k=length))

    def go_back(self):
        self.driver.back()

    def maximize_window(self):
        self.driver.maximize_window()

    def sleep_for_5_seconds(self):
        time.sleep(5)