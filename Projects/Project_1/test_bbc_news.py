from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Projects.Project_1.pages.main_page import MainPage
from Projects.Project_1.pages.news_page import NewsPage
from Projects.Project_1.pages.india_news_page import IndiaNewsPage

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)

print("hello i am working")
main_page = MainPage(driver)
news_page = NewsPage(driver)
india_news_page = IndiaNewsPage(driver)

print("hello i am working")

def test_bbc():
    print("hello i am working")
    main_page.open_bbc_website()
    main_page.go_full_screen()
    main_page.reject_cookies()
    main_page.click_news_tab()
    news_page.click_world_news_link()
    news_page.click_asia_news_link()
    news_page.click_india_news_link()
    india_news_page.print_headlines()
    driver.quit()
