from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
<<<<<<< HEAD
from selenium.webdriver.support import expected_conditions as ec
import time
import datetime

# Set up Chrome options to run in detached mode
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

# Start a new Chrome instance
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the BBC News website
driver.get("https://www.bbc.com")

time.sleep(1)
# Find and click the "Do not consent" button to accept cookies
reject_button = driver.find_element(by=By.XPATH, value="//*[@aria-label='Do not consent']")
reject_button.click()

# Find and click the "News" tab
news_tab = driver.find_element(by=By.XPATH, value="//a[text()='News']")
news_tab.click()

# use WebDriverWait to wait for each link to appear, then click them
wait = WebDriverWait(driver, 10)
world_link = wait.until(ec.presence_of_element_located((By.LINK_TEXT, "World")))
world_link.click()

asia_link = wait.until(ec.presence_of_element_located((By.LINK_TEXT, "Asia")))
asia_link.click()

india_link = wait.until(ec.presence_of_element_located((By.LINK_TEXT, "India")))
india_link.click()

# scrape headlines from India section and print them with current date and time

headlines_section = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '.lx-stream__feed')))
time.sleep(5)
headlines = headlines_section.find_elements(By.CSS_SELECTOR, "h3 a")

now = datetime.datetime.now()

print("Headlines from India,", now.strftime("%Y-%m-%d %H:%M:%S"))

for i, headline in enumerate(headlines, 1):
    print(f"{i}. {headline.text}")

driver.quit()
=======
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.bbc.com")

reject_button = driver.find_element(by=By.XPATH, value="//*[@aria-label='Do not consent']")
reject_button.click()

news_tab = driver.find_element(by=By.XPATH, value="//a[text()='News']")
news_tab.click()

world_link = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.LINK_TEXT, "World"))
)
world_link.click()

asia_link = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".gs-o-list-ui__item--flush.gel-long-primer.gs-u-display-block.gs-u-float-left.nw-c-nav__secondary-menuitem-container a[href='/news/world/asia']"))
 )
asia_link.click()

india_link = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.LINK_TEXT, "India"))
)
india_link.click()

element1 = driver.find_element(By.XPATH, value='//*[@id="topos-component"]/div[3]/div[2]/div[1]/div/div/div/div[3]/div')
text1 = element1.text

print(text1)

driver.close()
>>>>>>> main/master
