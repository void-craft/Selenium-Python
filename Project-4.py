from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#keeps the browser open
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

#goes to google.com
browser = webdriver.Chrome(options=chrome_options)
browser.get("https://www.google.com")

#rejects cookies by clicking the button
reject_cookies = browser.find_element(by=By.ID, value="W0wltc")
reject_cookies.click()

#finds the text box, enters a value and presses Enter key
text_box = browser.find_element(by=By.NAME, value="q")
text_box.send_keys("cute black cats")
text_box.send_keys(Keys.RETURN)

#finds the image tab, clicks it
image_tab = browser.find_element(by=By.LINK_TEXT, value="Imágenes")
image_tab.click()
