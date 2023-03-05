from selenium.webdriver.common.by import By
from Projects.Project_3.pages.base_page import BasePage

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.open_website = "https://magento.softwaretestingboard.com"
        self.create_account_link = (By.LINK_TEXT, "Create an Account")
        self.women_dropdown = (By.LINK_TEXT, "Women")
        self.top_expansion = (By.ID, "ui-id-9")
        self.hoodies_link = (By.ID, "ui-id-12")
        self.gear_dropdown = (By.LINK_TEXT, "Gear")
        self.watch_link = (By.LINK_TEXT, "Watches")
        self.sales_link = (By.XPATH, '//*[@id="ui-id-8"]/span')

    def open_magneto_website(self):
        self.driver.get(self.open_website)

    def maximize_window(self):
        self.driver.maximize_window()

    def click_element(self, create):
        self.wait_for_element(self.create_account_link).click()
    def navigate_to_hoodies(self):
        women_dropdown = self.wait_for_element(self.women_dropdown)
        self.action.move_to_element(women_dropdown).perform()

        top_expansion = self.wait_for_element(self.top_expansion)
        self.action.move_to_element(top_expansion).perform()

        self.wait_for_element(self.hoodies_link).click()
    def navigate_to_watches(self):
        gear_dropdown = self.wait_for_element(self.gear_dropdown)
        self.action.move_to_element(gear_dropdown).perform()

        self.wait_for_element(self.watch_link).click()

    def navigate_to_sales(self):
        sales_link = self.wait_for_element(self.sales_link)
        sales_link.click()






