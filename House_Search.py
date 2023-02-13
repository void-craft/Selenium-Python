from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
drive = webdriver.Chrome(options=chrome_options)

# Initialize the webdriver
driver = webdriver.Chrome()

# Open the website
driver.get("https://www.pisocompartido.com")

cookie_settings = driver.find_element(by=By.ID, value="didomi-notice-learn-more-button")
cookie_settings.click()


language = driver.find_element(by=By.XPATH, value="//*[@id="main-header"]/div/nav/div/span/span[1]")
language.click()

english = driver.find_element(by=By.CLASS_NAME, value="flag lang-en")
english.click()



# Reject the cookies
cookie_banner = driver.find_element(By.CSS_SELECTOR, ".cookie-notice__close")
cookie_banner.click()

# Find the search bar and enter the search query
search_bar = driver.find_element(By.ID, "main-search-keywords")
search_bar.send_keys("apartment Gijón to rent")
search_bar.submit()

# Wait for the page to load
time.sleep(2)

# Set the price range
price_filter = driver.find_element(By.CSS_SELECTOR, ".range-filter__input")
price_filter.click()
price_filter_min = driver.find_element(By.CSS_SELECTOR, ".filter-dialog__option[value='500']")
price_filter_min.click()
price_filter_max = driver.find_element(By.CSS_SELECTOR, ".filter-dialog__option[value='1000']")
price_filter_max.click()
price_filter_apply = driver.find_element(By.CSS_SELECTOR, ".filter-dialog__apply")
price_filter_apply.click()

# Wait for the page to load
time.sleep(2)

# Find the first result
result = driver.find_element(By.CSS_SELECTOR, ".item-link")
result.click()

# Wait for the page to load
time.sleep(2)

# Extract the details
title = driver.find_element(By.CSS_SELECTOR, ".core-header-property h1").text
price = driver.find_element(By.CSS_SELECTOR, ".core-price-standard").text
location = driver.find_element(By.CSS_SELECTOR, ".core-header-property h3").text
description = driver.find_element(By.CSS_SELECTOR, ".core-text-properties").text

# Print the details
print("Title:", title)
print("Price:", price)
print("Location:", location)
print("Description:", description)

# Close the webdriver
driver.close()