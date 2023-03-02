from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CompletePage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.postal_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.finish_button = (By.ID, "finish")
        self.subtotal_label = (By.CLASS_NAME, "summary_subtotal_label")
        self.total_label = (By.CLASS_NAME, "summary_total_label")
        self.message_text = (By.CLASS_NAME, "complete-header")

    def enter_first_name(self, first_name):
        field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.first_name_field))
        field.click()
        field.send_keys(first_name)

    def enter_last_name(self, last_name):
        field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.last_name_field))
        field.click()
        field.send_keys(last_name)

    def enter_postal_code(self, postal_code):
        field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.postal_code_field))
        field.click()
        field.send_keys(postal_code)

    def click_continue(self):
        button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.continue_button))
        button.click()

    def get_subtotal(self):
        label = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.subtotal_label))
        return float(label.text.strip("$"))

    def get_total(self):
        label = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.total_label))
        return float(label.text.strip("$"))

    def click_finish(self):
        button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.finish_button))
        button.click()

    def get_complete_message(self):
        return self.driver.find_element(*self.message_text).text

# XPATH //*[@id="checkout_complete_container"]/h2
# complete XPATH /html/body/div/div/div/div[2]/h2
# Class complete-header
