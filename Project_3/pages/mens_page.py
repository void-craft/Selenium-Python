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
        color_filter = self.wait_for_element(self.color_filter)
        color_filter.click()
        color_picker = self.wait_for_element(self.color_picker)
        color_picker.click()

    def add_shorts_to_compare(self):
        shorts1_locator = self.wait_for_element(self.shorts1_locator)
        self.action.move_to_element(shorts1_locator).perform()

        shorts1_to_compare = self.wait_for_element(self.shorts1_to_compare)
        shorts1_to_compare.click()

        shorts2_locator = self.wait_for_element(self.shorts2_locator)
        self.action.move_to_element(shorts2_locator).perform()

        shorts2_to_compare = self.wait_for_element(self.shorts2_to_compare)
        shorts2_to_compare.click()

    def go_to_comparison_page(self):
        comparison_link = self.wait_for_element(self.comparison_link)
        comparison_link.click()


