from selenium.webdriver.common.by import By
from Project_4.base_page import BasePage
class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.website_url = "https://www.google.com/?hl=en"
        self.reject_cookie_locator = (By.ID, "W0wltc")
        self.search_box = (By.NAME, "q")
        self.query_text = "Chennai"

    def go_to_website(self):
        self.open_website(self.website_url)

    def reject_cookies(self):
        self.start_time()
        reject_cookies = self.wait_for_element(self.reject_cookie_locator)
        reject_cookies.click()
        cookie_time = self.end_time()
        print("Time Taken to Reject Cookies: ", cookie_time)

    def search_for(self):
        search_box = self.wait_for_element(self.search_box)
        self.add_text(self.search_box, self.query_text)
        self.start_time()
        search_box.submit()
        search_time = self.end_time()
        print("Time Taken to Complete Search: ", search_time)
        self.driver.save_screenshot(f"{self.search_box}_web.png")

    def go_full_screen(self):
        self.maximize_window()
