import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Meera/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service= service_obj)
driver.get("https://www.amazon.com/")

searchbar = driver.find_element(By.XPATH,'//*[(@id = "twotabsearchtextbox")]')
searchbar.send_keys ("hairdryer")
searchbar.send_keys(Keys. ENTER)


driver.close()