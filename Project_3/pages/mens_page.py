from selenium.webdriver.common.by import By
from Projects.Project_3.pages.base_page import BasePage
class MensPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.color_filter = (By.XPATH, '//*[@id="narrow-by-list"]/div[4]/div[1]')
        self.color_picker = (By.XPATH, '//*[@id="narrow-by-list"]/div[4]/div[2]/div/div/a[1]/div')
        self.shorts1_locator = (By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[2]/div/a/span/span/img')
        self.shorts1_to_compare = (By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[2]/div/div/div[4]/div/div[2]/a[2]')
        self.shorts2_locator = (By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[1]/div/a/span/span/img')
        self.shorts2_to_compare = (By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[1]/div/div/div[3]/div/div[2]/a[2]')
        self.comparison_link = (By.XPATH, '//*[@id="maincontent"]/div[2]/div[2]/div/div/div/a')

    def filter_by_color(self):
        self.click_element(self.color_filter)
        self.click_element(self.color_picker)
    def add_shorts_to_compare(self):
        self.hover(self.shorts1_locator)
        self.click_element(self.shorts1_to_compare)
        self.hover(self.shorts2_locator)
        self.click_element(self.shorts2_to_compare)

    def go_to_comparison_page(self):
        self.click_element(self.comparison_link)


