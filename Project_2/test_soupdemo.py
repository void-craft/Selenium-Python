def test_soap_demo():
    from selenium.webdriver.chrome.options import Options
    from selenium import webdriver
    from Projects.Project_2.pages.login_page import LoginPage
    from Projects.Project_2.pages.products_page import ProductsPage
    from Projects.Project_2.pages.cart_page import CartPage
    from Projects.Project_2.pages.checkout_page import CheckoutPage
    from Projects.Project_2.pages.complete_page import CompletePage
    from Projects.Project_2.pages.product_details_page import ProductDetailsPage

    chrome_options = Options()
    chrome_options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=chrome_options)

    login_page = LoginPage(driver)
    login_page.go_to()
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(driver)
    products_page.add_to_cart("Sauce Labs Bike Light")

    products_page = ProductsPage(driver)
    products_page.add_to_cart("Sauce Labs Backpack")

    products_page.go_to_cart()

    cart_page = CartPage(driver)
    subtotal = cart_page.calculate_subtotal()
    cart_page.checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.enter_information("Hema", "Priya", "33011")

    complete_page = CompletePage(driver)
    checkout_subtotal = checkout_page.get_subtotal()

    assert subtotal == checkout_subtotal, f"Subtotal doesn't match. Cart: {subtotal} Checkout: {checkout_subtotal}"
    print(f"Displayed Subtotal {checkout_subtotal} matches the Expected Subtotal {subtotal}")

    checkout_total = checkout_page.get_total()
    assert str(checkout_total) == "43.18", f"Total doesn't match. Expected: $43.18 Actual: {checkout_total}"
    print(f"Expected total of $43.18 matches the actual total of ${checkout_total}")

    checkout_page.click_finish()

    assert complete_page.get_complete_message() == "Thank you for your order!", "Complete message doesn't match."

    driver.quit()
