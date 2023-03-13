from selenium.webdriver.common.by import By
from Project_3.pages.base_page import BasePage

class HoodiesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.sorter_locator = (By.XPATH, '//*[@id="sorter"]')
        self.sort_by_price_locator = (By.XPATH, '//*[@class="sorter-options"]/option[@value="price"]')
        self.hoodie1_locator = (By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[12]/div/a/span/span/img')
        self.hoodie2_locator = (By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[11]/div/a/span/span/img')
        self.hoodie1_to_favorite = (By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[12]/div/div/div[4]/div/div[2]/a[1]')
        self.hoodie2_to_favorite = (By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[11]/div/div/div[3]/div/div[2]/a[1]')
        self.gear_dropdown = (By.LINK_TEXT, "Gear")
        self.watch_link = (By.LINK_TEXT, "Watches")

    def sort_hoodies(self):
        self.click_element(self.sorter_locator)
        self.click_element(self.sort_by_price_locator)
    def add_hoodies_to_favorite(self):
        self.hover(self.hoodie1_locator)
        self.click_element(self.hoodie1_to_favorite)
        self.driver.back()
        self.hover(self.hoodie2_locator)
        self.click_element(self.hoodie2_to_favorite)
    def navigate_to_watches(self):
        self.hover(self.gear_dropdown)
        self.click_element(self.watch_link)







