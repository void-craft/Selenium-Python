from selenium.webdriver.common.by import By
from Projects.Project_3.pages.base_page import BasePage

class WatchesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.watch_locator = (By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[1]/div/a/span/span/img')
        self.watch_to_cart = (By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[1]/div/div/div[3]/div/div[1]/form/button/span')
        self.sales_link = (By.XPATH, '//*[@id="ui-id-8"]/span')
    def add_watch_to_cart(self):
        self.hover(self.watch_locator)
        self.click_element(self.watch_to_cart)

    def navigate_to_sales(self):
        self.click_element(self.sales_link)