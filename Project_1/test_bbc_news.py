from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Projects.Project_1.pages.main_page import MainPage
from Projects.Project_1.pages.news_page import NewsPage
from Projects.Project_1.pages.india_news_page import IndiaNewsPage

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
main_page = MainPage(driver)
news_page = NewsPage(driver)
india_news_page = IndiaNewsPage(driver)
def test_bbc_news():
    main_page.load_page("https://www.bbc.com")

    main_page.reject_cookies()

    main_page.go_to_news_page()

    news_page.go_to_world_news_page()

    news_page.go_to_asia_news_page()

    news_page.go_to_india_news_page()

    india_news_page.get_headlines()

    driver.quit()
