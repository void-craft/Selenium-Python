import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://magento.softwaretestingboard.com/")
driver.maximize_window()

# account creation
create_account = driver.find_element(by=By.LINK_TEXT, value="Create an Account")
create_account.click()
first_name = driver.find_element(by=By.ID, value="firstname")
first_name.send_keys("Void")
last_name = driver.find_element(by=By.ID, value="lastname")
last_name.send_keys("Meow")
email_id = driver.find_element(by=By.ID, value="email_address")
#
email_id.send_keys("cannotsay12345678@gmail.com")
password_enter = driver.find_element(by=By.ID, value="password")
password_enter.send_keys("Themeowvil!")
confirm_password_enter = driver.find_element(by=By.ID, value="password-confirmation")
confirm_password_enter.send_keys("Themeowvil!")
complete_creation = driver.find_element(by=By.CLASS_NAME, value="primary")
complete_creation.click()

# hovering over categories to find hoodies
hover = ActionChains(driver)
women_dropdown = driver.find_element(by=By.LINK_TEXT, value="Women")
hover.move_to_element(women_dropdown).perform()
top_expansion = driver.find_element(by=By.ID, value="ui-id-9")
hover.move_to_element(top_expansion).perform()

# clicking hoodies
hoodies = driver.find_element(by=By.ID, value="ui-id-12")
hoodies.click()

# sorting hoodies by price
sort_by = Select(driver.find_element(by=By.ID, value="sorter"))
sort_by.select_by_value("price")

item1 = driver.find_element(by=By.XPATH, value='//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[12]/div/a/span/span/img')
hover.move_to_element(item1).perform()
favorite1 = item1.find_element(by=By.XPATH, value='//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[12]/div/div/div[4]/div/div[2]/a[1]')
hover.move_to_element(favorite1).click().perform()

driver.back()

item2 = driver.find_element(by=By.XPATH, value='//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[11]/div/a/span/span/img')
hover.move_to_element(item2).perform()
favorite2 = item2.find_element(by=By.XPATH, value='//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[11]/div/div/div[3]/div/div[2]/a[1]')
hover.move_to_element(favorite2).click().perform()

gear = driver.find_element(by=By.LINK_TEXT, value="Gear")
hover.move_to_element(gear).perform()
time.sleep(2)
watches = driver.find_element(by=By.LINK_TEXT, value="Watches")
hover.move_to_element(watches).click().perform()

item3 = driver.find_element(by=By.XPATH, value='//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[1]/div/a/span/span/img')
hover.move_to_element(item3).perform()
time.sleep(2)
item1_add = item3.find_element(by=By.XPATH, value='//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[1]/div/div/div[3]/div/div[1]/form/button/span')
hover.move_to_element(item1_add).click().perform()

