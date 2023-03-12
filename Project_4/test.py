from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Project_4.pages.home_page import HomePage
from Project_4.pages.result_page import ResultPage

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument("--lang=en")
driver = webdriver.Chrome(options=chrome_options)

home_page = HomePage(driver)

def test():
    home_page.go_to_website()
    home_page.go_full_screen()
    home_page.reject_cookies()
    home_page.search_for()

    driver.quit()






