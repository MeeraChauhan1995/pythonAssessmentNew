import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Meera/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service= service_obj)
driver.get("https://www.amazon.com/")


driver.find_element(By.ID, 'nav-search-dropdown-card').click()
time.sleep(3)
drp = []
Droplist = driver.find_element(By.XPATH, '//*[@id="searchDropdownBox"]')
print(Droplist.text)
