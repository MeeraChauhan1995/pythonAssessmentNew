import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Meera/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service= service_obj)
driver.get("https://www.amazon.com/")

driver.find_element(By.ID, 'nav-cart-count').click()
errmsg= driver.find_element(By.ID, 'sc-active-cart').text
print(errmsg)

time.sleep(3)
driver.close()