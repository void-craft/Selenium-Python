from selenium.webdriver.common.by import By
from Projects.Project_2.pages.base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, 'first-name')
    LAST_NAME_INPUT = (By.ID, 'last-name')
    POSTAL_CODE_INPUT = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')
    FINISH_BUTTON = (By.ID, 'finish')
    SUBTOTAL_LABEL = (By.XPATH, "//div[@class='summary_subtotal_label']")
    TOTAL_LABEL = (By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[8]')

    def enter_information(self, first_name, last_name, postal_code):
        self.enter_text(self.FIRST_NAME_INPUT, first_name)
        self.enter_text(self.LAST_NAME_INPUT, last_name)
        self.enter_text(self.POSTAL_CODE_INPUT, postal_code)
        self.click(self.CONTINUE_BUTTON)

    def enter_text(self, locator, text):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

    def get_subtotal(self):
        subtotal_text = self.driver.find_element(*self.SUBTOTAL_LABEL).text
        subtotal_value = subtotal_text.split(': ')[1].replace('$', '')
        return float(subtotal_value)

    def get_total(self):
        total_text = self.driver.find_element(*self.TOTAL_LABEL).text
        total_value = total_text.split(': ')[1].replace('$', '')
        return float(total_value)

    def click_finish(self):
        self.click(self.FINISH_BUTTON)
