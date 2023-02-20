from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)

# Load the page
driver.get("https://magento.softwaretestingboard.com/women/tops-women/hoodies-and-sweatshirts-women.html")


# Wait for the product list to load
wait = WebDriverWait(driver, 10)
product_list = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "products.list.items.product-items")))

# locate and click the last item's "Add to Wishlist" button
last_item = product_list.find_elements_by_class_name("product-item")[-1]
wishlist_button = last_item.find_element_by_class_name("action.towishlist")
wishlist_button.click()

# locate and click the second to the last item's "Add to Wishlist" button
second_last_item = product_list.find_elements_by_class_name("product-item")[-2]
wishlist_button = second_last_item.find_element_by_class_name("action.towishlist")
wishlist_button.click()
