import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://magento.softwaretestingboard.com/")

driver.maximize_window()
# generate random email address
def generate_random_email():
    random_string = ''.join(random.choices(string.ascii_lowercase, k=10))
    random_email_address = f"{random_string}@example.com"
    return random_email_address

# account creation
create_account = driver.find_element(by=By.LINK_TEXT, value="Create an Account")
create_account.click()
first_name = driver.find_element(by=By.ID, value="firstname")
first_name.send_keys("Void")
last_name = driver.find_element(by=By.ID, value="lastname")
last_name.send_keys("Meow")
email_id = driver.find_element(by=By.ID, value="email_address")
random_email = generate_random_email()
email_id.send_keys(random_email)
password_enter = driver.find_element(by=By.ID, value="password")
password_enter.send_keys("Themeowvil!")
confirm_password_enter = driver.find_element(by=By.ID, value="password-confirmation")
confirm_password_enter.send_keys("Themeowvil!")
complete_creation = driver.find_element(by=By.CLASS_NAME, value="primary")
complete_creation.click()
time.sleep(1)

wait = WebDriverWait(driver, 5)
hover = ActionChains(driver)

# hovers over dropdown "Women", then to "Top"
women_dropdown = driver.find_element(by=By.LINK_TEXT, value="Women")
hover.move_to_element(women_dropdown).perform()
top_expansion = driver.find_element(by=By.ID, value="ui-id-9")
hover.move_to_element(top_expansion).perform()
# clicks hoodies
hoodies = wait.until(
    EC.presence_of_element_located((By.ID, "ui-id-12"))
)
hoodies.click()

# sorting hoodies by price
sort_by = Select(driver.find_element(by=By.ID, value="sorter"))
sort_by.select_by_value("price")

# finds the last item on the page hovering, then clicks the Add to Favorites icon
hoodie1 = driver.find_element(by=By.XPATH, value='//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[12]/div/a/span/span/img')
hover.move_to_element(hoodie1).perform()
hoodie1_fav = driver.find_element(by=By.XPATH, value='//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[12]/div/div/div[4]/div/div[2]/a[1]')
hover.move_to_element(hoodie1_fav).click().perform()

# Going back to hoodies page from favorites
driver.back()

# finds another item and clicks the Add to Favorites icon
hoodie2 = driver.find_element(by=By.XPATH, value='//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[11]/div/a/span/span/img')
hover.move_to_element(hoodie2).perform()
hoodie2_fav = driver.find_element(by=By.XPATH, value='//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[11]/div/div/div[3]/div/div[2]/a[1]')
hover.move_to_element(hoodie2_fav).click().perform()

driver.back()

wait = WebDriverWait(driver, 5)
# hovers over gear, clicks watches from the dropdown
gear = wait.until(
    EC.presence_of_element_located((By.ID, "ui-id-6"))
)
hover.move_to_element(gear).perform()
time.sleep(3)
watches = driver.find_element(by=By.LINK_TEXT, value="Watches")
watches.click()
# hovers over an item and clicks the Add to Cart button
watch1 = wait.until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[1]/div/a/span/span/img'))
)
hover.move_to_element(watch1).perform()
time.sleep(2)
watch_add = WebDriverWait(watch1, 2).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[1]/div/div/div[3]/div/div[1]/form/button/span'))
)
watch_add.click()

# clicks Sale category
sale = wait.until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="ui-id-8"]/span'))
)
sale.click()

men_deal = driver.find_element(by=By.CLASS_NAME, value="block-promo.sale-mens")
men_deal.click()

# clicking "Color" filter and then selecting the black swatch to filter
color_filter = driver.find_element(by=By.XPATH, value='//*[@id="narrow-by-list"]/div[4]/div[1]')
color_filter.click()
color_picker = color_filter.find_element(by=By.XPATH, value='//*[@id="narrow-by-list"]/div[4]/div[2]/div/div/a[1]/div')
color_picker.click()

# hover over shorts image to activate the comparison icon and then clicking the icon
shorts1 = driver.find_element(by=By.XPATH, value='//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[2]/div/a/span/span/img')
hover.move_to_element(shorts1).perform()
shorts1_compare = shorts1.find_element(by=By.XPATH, value='//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[2]/div/div/div[4]/div/div[2]/a[2]')
shorts1_compare.click()

# selecting another shorts to compare
shorts2 = driver.find_element(by=By.XPATH, value='//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[1]/div/a/span/span/img')
hover.move_to_element(shorts2).perform()
shorts2_compare = shorts2.find_element(by=By.XPATH, value='//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[1]/div/div/div[3]/div/div[2]/a[2]')
shorts2_compare.click()

time.sleep(1)
#link_css_selector = "a[title='Compare Products']"
# clicking the comparison link
comparison = wait.until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="maincontent"]/div[2]/div[2]/div/div/div/a'))
)
comparison.click()

# clicking one of the item's Add to Cart button
shorts1_add = driver.find_element(by=By.XPATH, value='//*[@id="product-comparison"]/tbody[1]/tr/td[1]/div[3]/div[1]/form/button/span')
shorts1_add.click()

# clicking size option for the item
shorts1_size = wait.until(
    EC.presence_of_element_located((By.ID, "option-label-size-143-item-177"))
)
shorts1_size.click()

# clicking the color option for the item
shorts1_color = driver.find_element(by=By.ID, value="option-label-color-93-item-49")
shorts1_color.click()

# locating the Qty text box and entering "2"
shorts1_qty = driver.find_element(by=By.ID, value="qty")
shorts1_qty.clear()
shorts1_qty.send_keys("2")

# adding the product to cart
shorts1_confirm_add = driver.find_element(by=By.ID, value="product-addtocart-button")
shorts1_confirm_add.click()
time.sleep(3)
# clicking the cart icon using class
cart = driver.find_element(by=By.CLASS_NAME, value="action.showcart")
cart.click()

# click proceed to checkout button using id
checkout = driver.find_element(by=By.ID, value="top-cart-btn-checkout")
checkout.click()

time.sleep(5)
address = driver.find_element(by=By.XPATH, value='/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form/div/fieldset/div/div[1]/div/input')
address.send_keys("Meow Meow Street, 3")
city = driver.find_element(by=By.XPATH, value='/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form/div/div[4]/div/input')
city.send_keys("Oviedo")
phone = driver.find_element(by=By.XPATH, value='/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form/div/div[9]/div/input')
phone.send_keys("987654321")
country = driver.find_element(by=By.XPATH, value='/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form/div/div[8]/div/select')
country.click()
country.send_keys("sp")
country.send_keys(Keys.RETURN)
time.sleep(3)
province = driver.find_element(By.XPATH, value='/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form/div/div[5]/div/select')
province.send_keys("as")
province.send_keys(Keys.RETURN)
zipcode = driver.find_element(by=By.XPATH, value='/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form/div/div[7]/div/input')
zipcode.send_keys("33010")
cont = driver.find_element(by=By.XPATH, value='/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[2]/div/div[3]/form/div[3]/div/button/span')
cont.click()
billing_address = wait.until(
    EC.presence_of_element_located((By.ID, "billing-address-same-as-shipping-checkmo"))
)
billing_address.click()
place_order = driver.find_element(by=By.XPATH, value='/html/body/div[3]/main/div[2]/div/div[2]/div[4]/ol/li[3]/div/form/fieldset/div[1]/div/div/div[2]/div[2]/div[4]/div/button')
place_order.click()
order_number = wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "order-number"))
)
print(f"Your order number is: {order_number.text}")