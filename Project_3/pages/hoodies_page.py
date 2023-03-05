from selenium.webdriver.common.by import By
from Projects.Project_3.pages.base_page import BasePage

class HoodiesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.sorter_locator = (By.XPATH, '//*[@id="sorter"]')
        self.sort_by_price_locator = (By.XPATH, '//*[@class="sorter-options"]/option[@value="price"]')
        self.hoodie1_locator = (By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[12]/div/a/span/span/img')
        self.hoodie2_locator = (By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[11]/div/a/span/span/img')
        self.hoodie1_to_favorite = (By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[12]/div/div/div[4]/div/div[2]/a[1]')
        self.hoodie2_to_favorite = (By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[11]/div/div/div[3]/div/div[2]/a[1]')
    def sort_hoodies(self):
        select_sorter = self.wait_for_element(self.sorter_locator)
        select_sorter.click()

        select_by_price = self.wait_for_element(self.sort_by_price_locator)
        select_by_price.click()

    def add_hoodies_to_favorite(self):
        hoodie1_locator = self.wait_for_element(self.hoodie1_locator)
        self.action.move_to_element(hoodie1_locator).perform()

        hoodie1_to_favorite = self.wait_for_element(self.hoodie1_to_favorite)
        hoodie1_to_favorite.click()

        self.driver.back()

        hoodie2_locator = self.wait_for_element(self.hoodie2_locator)
        self.action.move_to_element(hoodie2_locator).perform()

        hoodie2_to_favorite = self.wait_for_element(self.hoodie2_to_favorite)
        hoodie2_to_favorite.click()




