from selenium.webdriver.common.by import By
from Projects.Project_3.pages.base_page import BasePage

class SalesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.mens_page = (By.CLASS_NAME, "block-promo.sale-mens")

    def go_to_mens_page(self):
        mens_page = self.wait_for_element(self.mens_page)
        mens_page.click()
