from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.google.com")

reject_cookies = driver.find_element(by=By.ID, value="W0wltc")
start_time1 = time.time()
reject_cookies.click()
cookie_time = time.time() - start_time1
print("Cookie Rejection time: ", cookie_time)

# Locating search box and entering "Chennai", clicking enter and calculating time until result, taking screenshot of the tab
search_box = driver.find_element(by=By.NAME, value="q")
search_box.send_keys("Chennai")
start_time2 = time.time()
search_box.submit()
search_time = time.time() - start_time2
print("Search time: ", search_time)
driver.save_screenshot("Chennai_web.png")

# Opening image tab, calculating time taken, taking screenshot, closing the tab
start_time3 = time.time()
images_link = driver.find_element(by=By.LINK_TEXT, value="Imágenes")
images_link.send_keys(Keys.CONTROL + Keys.RETURN)
driver.switch_to.window(driver.window_handles[1])
image_time = time.time() - start_time3
print("Images time: ", image_time)
driver.save_screenshot("Chennai_images.png")
driver.close()
driver.switch_to.window(driver.window_handles[0])

# Opening news tab, calculating time taken, taking screenshot, closing the tab
start_time4 = time.time()
news_link = driver.find_element(by=By.LINK_TEXT, value="Noticias")
news_link.send_keys(Keys.CONTROL + Keys.RETURN)
driver.switch_to.window(driver.window_handles[1])
news_time = time.time() - start_time4
print("News time: ", news_time)
driver.save_screenshot("news.png")
driver.close()
driver.switch_to.window(driver.window_handles[0])


# Opening news tab, calculating time taken, taking screenshot, closing the tab
start_time5 = time.time()
maps_link = driver.find_element(by=By.LINK_TEXT, value="Maps")
maps_link.send_keys(Keys.CONTROL + Keys.RETURN)
driver.switch_to.window(driver.window_handles[1])
map_time = time.time() - start_time5
print("Maps time: ", map_time)
driver.save_screenshot("maps.png")
driver.close()
driver.switch_to.window(driver.window_handles[0])

driver.quit()
