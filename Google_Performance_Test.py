from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.google.com")

start_time1 = time.time()

reject_cookies = driver.find_element(by=By.ID, value="W0wltc")
reject_cookies.click()

cookie_time = time.time() - start_time1
print("Cookie Rejection time: ", cookie_time)

start_time2 = time.time()

search_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "q")))
search_box.send_keys("Chennai")
search_box.submit()

wait = WebDriverWait(driver, 10)
wait.until(EC.title_contains("Chennai"))

search_time = time.time() - start_time2
print("Search time: ", search_time)

start_time3 = time.time()

images_link = driver.find_element(by=By.LINK_TEXT, value="Imágenes")
images_link.send_keys(Keys.CONTROL + Keys.RETURN)
driver.switch_to.window(driver.window_handles[1])
driver.save_screenshot("images.png")
driver.close()
driver.switch_to.window(driver.window_handles[0])

image_time = time.time() - start_time3
print("Images time: ", image_time)

start_time4 = time.time()

news_link = driver.find_element(by=By.LINK_TEXT, value="Noticias")
news_link.send_keys(Keys.CONTROL + Keys.RETURN)
driver.switch_to.window(driver.window_handles[1])
driver.save_screenshot("news.png")
driver.close()
driver.switch_to.window(driver.window_handles[0])

news_time = time.time() - start_time4
print("News time: ", news_time)

start_time5 = time.time()

maps_link = driver.find_element(by=By.LINK_TEXT, value="Maps")
maps_link.send_keys(Keys.CONTROL + Keys.RETURN)
driver.switch_to.window(driver.window_handles[1])
driver.save_screenshot("maps.png")
driver.close()
driver.switch_to.window(driver.window_handles[0])

map_time = time.time() - start_time5
print("Maps time: ", map_time)

driver.quit()