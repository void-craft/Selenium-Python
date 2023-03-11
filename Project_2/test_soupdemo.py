from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from Projects.Project_2.pages.login_page import LoginPage
from Projects.Project_2.pages.products_page import ProductsPage
from Projects.Project_2.pages.cart_page import CartPage
from Projects.Project_2.pages.checkout_page import CheckoutPage
from Projects.Project_2.pages.complete_page import CompletePage

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)

login_page = LoginPage(driver)
products_page = ProductsPage(driver)
cart_page = CartPage(driver)
checkout_page = CheckoutPage(driver)
complete_page = CompletePage(driver)

def test_soap_demo():
    login_page.go_to()
    login_page.enter_username()
    login_page.enter_password()
    login_page.click_login()
    products_page.add_products_to_cart()
    products_page.go_to_cart()

    cart_subtotal = cart_page.calculate_subtotal()

    cart_page.click_checkout()
    checkout_page.enter_information()

    checkout_subtotal = checkout_page.get_subtotal()

    assert cart_subtotal == checkout_subtotal, f"Subtotal doesn't match. Cart: {cart_subtotal} Checkout: {checkout_subtotal}"
    print(f"Displayed Subtotal {checkout_subtotal} matches the Expected Subtotal {cart_subtotal}")

    checkout_total = checkout_page.get_total()
    assert str(checkout_total) == "43.18", f"Total doesn't match. Expected: $43.18 Actual: $ {checkout_total}"
    print(f"Expected total of $43.18 matches the actual total of ${checkout_total}")

    checkout_page.click_finish()
    assert complete_page.get_complete_message() == "Thank you for your order!", "Complete message doesn't match."

    driver.quit()
