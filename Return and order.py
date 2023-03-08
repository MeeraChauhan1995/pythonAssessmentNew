import time

from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

service_obj = Service("C:/Meera/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service= service_obj)
driver.get("https://www.amazon.com/")
time.sleep(3)
driver.find_element(By.ID, 'nav-orders').click()
driver.find_element(By.ID, 'ap_email').send_keys('6476875247')
driver.find_element(By.ID, 'continue').click()

driver.find_element(By.ID, 'ap_password').send_keys('Chauhan@1095')
driver.find_element(By.ID, 'auth-signin-button').click()
time.sleep(3)

driver.find_element(By.CLASS_NAME, 'a-dropdown-prompt').click()
items= driver.find_elements(By.XPATH, '//div[@class="a-popover-inner"][1]')
time.sleep(3)
selectitem= driver.find_element(By.XPATH, '//*[@id="a-page"]/section/div/div[8]').text
print(selectitem)

driver.find_element(By.LINK_TEXT, 'Buy Again').click()

driver.find_element(By.LINK_TEXT, 'Not Yet Shipped').click()

driver.find_element(By.LINK_TEXT, 'Cancelled Orders').click()

driver.close()