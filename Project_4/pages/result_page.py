from selenium.webdriver.common.by import By
from Project_4.base_page import BasePage
class ResultPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.image_link = (By.LINK_TEXT, "Images")

    def open_images_tab(self):
        self.start_time()
        self.click_element(self.image_link)

        images_link.send_keys(Keys.CONTROL + Keys.RETURN)
        self.driver.switch_to.window(self.driver.window_handles[1])
        image_time = self.end_time()
        print("Images time: ", image_time)
        self.driver.save_screenshot(f"{self.image_link}_web.png")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
