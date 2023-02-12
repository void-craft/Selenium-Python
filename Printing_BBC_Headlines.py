from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
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

india_link = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.LINK_TEXT, "India"))
)
india_link.click()

time.sleep(5)

element1 = driver.find_element(By.XPATH, value='//*[@id="topos-component"]/div[3]/div[2]/div[1]/div/div/div/div[3]/div')
text1 = element1.text

print(text1)

driver.close()