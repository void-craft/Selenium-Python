from selenium.webdriver.common.by import By
from Project_3.pages.base_page import BasePage

class ComparisonPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.shorts_add = (By.XPATH, '//*[@id="product-comparison"]/tbody[1]/tr/td[1]/div[3]/div[1]/form/button/span')

    def add_shorts_expansion(self):
        self.click_element(self.shorts_add)
