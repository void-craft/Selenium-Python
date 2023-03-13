from selenium.webdriver.common.by import By
from Project_2.pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.first_name_locator = (By.ID, 'first-name')
        self.last_name_input = (By.ID, 'last-name')
        self.postal_code_input = (By.ID, 'postal-code')
        self.continue_button = (By.ID, 'continue')
        self.finish_button = (By.ID, 'finish')
        self.subtotal_label = (By.XPATH, "//div[@class='summary_subtotal_label']")
        self.total_label = (By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[8]')

    def enter_information(self):
        self.input_text(self.first_name_locator, "Void")
        self.input_text(self.last_name_input, "Craft")
        self.input_text(self.postal_code_input, "33333")
        self.click_element(self.continue_button)

    def get_subtotal(self):
        subtotal_text = self.wait_for_element(self.subtotal_label).text
        subtotal_value = subtotal_text.split(': ')[1].replace('$', '')
        return float(subtotal_value)

    def get_total(self):
        total_text = self.wait_for_element(self.total_label).text
        total_value = total_text.split(': ')[1].replace('$', '')
        return float(total_value)

    def click_finish(self):
        self.click_element(self.finish_button)
