from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keeps the browser open
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)

# opens an instance of the browser
driver.get("https://www.saucedemo.com/")

# logins using username and password
username = driver.find_element(by=By.ID, value="user-name")
username.click()
username.send_keys("standard_user")
username.send_keys(Keys.TAB)

password = driver.find_element(by=By.ID, value="password")
password.send_keys("secret_sauce")
password.send_keys(Keys.TAB, Keys.ENTER)


open_backpack = driver.find_element(by=By.ID, value="item_4_title_link")
open_backpack.click()

add_backpack = driver.find_element(by=By.ID, value="add-to-cart-sauce-labs-backpack")
add_backpack.click()

find_backpack_name = driver.find_element(by=By.CLASS_NAME, value="inventory_details_name.large_size")
name_backpack = find_backpack_name.text
print(f"Product Name: {name_backpack}")

find_backpack_price = driver.find_element(by=By.CLASS_NAME, value="inventory_details_price")
price_backpack = find_backpack_price.text.strip('$')
print(f"Produce Price: {price_backpack}")

go_back_button = driver.find_element(by=By.ID, value="back-to-products")
go_back_button.click()

open_tshirt = driver.find_element(by=By.ID, value="item_1_title_link")
open_tshirt.click()

add_tshirt = driver.find_element(by=By.ID, value="add-to-cart-sauce-labs-bolt-t-shirt")
add_tshirt.click()

find_tshirt_name = driver.find_element(by=By.CLASS_NAME, value="inventory_details_name.large_size")
name_tshirt = find_tshirt_name.text
print(f"Product Name: {name_tshirt}")

find_tshirt_price = driver.find_element(by=By.CLASS_NAME, value="inventory_details_price")
price_tshirt = find_tshirt_price.text.strip('$')
print(f"Produce Price: {price_tshirt}")

select_checkout = driver.find_element(by=By.CLASS_NAME, value="shopping_cart_link")
select_checkout.click()

select_checkout = driver.find_element(by=By.ID, value="checkout")
select_checkout.click()

first_name = driver.find_element(by=By.ID, value="first-name")
first_name.click()
first_name.send_keys("Hema")
first_name.send_keys(Keys.TAB)

last_name = driver.find_element(by=By.ID, value="last-name")
last_name.send_keys("Priya")
last_name.send_keys(Keys.TAB)

postal_code = driver.find_element(by=By.ID, value="postal-code")
postal_code.send_keys(33011)
postal_code.send_keys(Keys.TAB)

continue_button = driver.find_element(by=By.ID, value="continue")
continue_button.click()

expected_subtotal = float(price_backpack) + float(price_tshirt)

subtotal_text = driver.find_element(by=By.CLASS_NAME, value="summary_subtotal_label").text
subtotal_number = float(subtotal_text.split("$")[1])

if expected_subtotal == subtotal_number:
    print(f"The expected subtotal of ${expected_subtotal} matches the shown subtotal.")
else:
    print(f"The expected subtotal of ${expected_subtotal} doesn't match the amount shown(${subtotal_number})")

total_text = driver.find_element(by=By.CLASS_NAME, value="summary_total_label").text
total_number = float(total_text.split("$")[1])

expected_total = 49.66

assert total_number == expected_total, f"Expected total: ${expected_total} doesn't match the actual total: ${total_number}"
print(f"The expected total ${expected_total} matches the actual total ${total_number} after tax.")

finish_button = driver.find_element(by=By.ID, value="finish")
finish_button.click()

driver.quit()

