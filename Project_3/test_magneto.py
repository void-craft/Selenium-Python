from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Projects.Project_3.pages.account_page import AccountPage
from Projects.Project_3.pages.hoodies_page import HoodiesPage
from Projects.Project_3.pages.main_page import MainPage
from Projects.Project_3.pages.base_page import BasePage
from Projects.Project_3.pages.watches_page import WatchesPage
from Projects.Project_3.pages.sales_page import SalesPage
from Projects.Project_3.pages.mens_page import MensPage
from Projects.Project_3.pages.comparison_page import ComparisonPage
from Projects.Project_3.pages.shorts_details_page import ShortsDetailsPage
from Projects.Project_3.pages.cart_page import CartPage

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
account_page = AccountPage(driver)
hoodies_page = HoodiesPage(driver)
main_page = MainPage(driver)
base_page = BasePage(driver)
watches_page = WatchesPage(driver)
sales_page = SalesPage(driver)
mens_page = MensPage(driver)
comparison_page = ComparisonPage(driver)
shorts_details_page = ShortsDetailsPage(driver)
cart_page = CartPage(driver)
def test_magneto():
    main_page.open_magneto_website()
    main_page.maximize_window()
    main_page.create_account()
    account_page.enter_first_name()
    account_page.enter_last_name()
    account_page.enter_email()
    account_page.enter_password()
    account_page.click_create_account_button()
    account_page.navigate_to_hoodies()
    hoodies_page.sort_hoodies()
    hoodies_page.add_hoodies_to_favorite()
    hoodies_page.navigate_to_watches()
    watches_page.add_watch_to_cart()
    watches_page.go_back()
    watches_page.navigate_to_sales()
    sales_page.go_to_mens_page()
    mens_page.filter_by_color()
    mens_page.add_shorts_to_compare()
    mens_page.go_to_comparison_page()
    comparison_page.add_shorts_expansion()
    shorts_details_page.add_shorts_to_cart()
    shorts_details_page.sleep_for_5_seconds()
    shorts_details_page.open_cart()
    cart_page.place_order()
    cart_page.get_order_number()
    driver.quit()
