from selenium.webdriver.common.by import By
from Project_2.pages.base_page import BasePage


class CompletePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.postal_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.finish_button = (By.ID, "finish")
        self.subtotal_label = (By.CLASS_NAME, "summary_subtotal_label")
        self.total_label = (By.CLASS_NAME, "summary_total_label")
        self.message_text = (By.CLASS_NAME, "complete-header")

    def enter_first_name(self):
        self.input_text(self.first_name_field, "Void")

    def enter_last_name(self):
        self.input_text(self.last_name_field, "Cart")

    def enter_postal_code(self):
        self.input_text(self.postal_code_field, "33333")

    def click_continue(self):
        self.click_element(self.continue_button)

    def get_subtotal(self):
        label = self.wait_for_element(self.subtotal_label)
        return float(label.text.strip("$"))

    def get_total(self):
        label = self.wait_for_element(self.total_label)
        return float(label.text.strip("$"))

    def click_finish(self):
        self.click_element(self.finish_button)

    def get_complete_message(self):
        return self.wait_for_element(self.message_text).text

