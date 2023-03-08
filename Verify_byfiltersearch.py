import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Meera/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service= service_obj)
driver.get("https://www.amazon.com/")
keyword = "Airtags"
search = driver.find_element(By.XPATH,'//*[(@id = "twotabsearchtextbox")]')
search.send_keys(keyword)
# click search button
search_button = driver.find_element(By.ID, 'nav-search-submit-button')
search_button.click()

#apply filter by brand
driver.implicitly_wait(5)
totalist = []
fiters = []
tots= driver.find_elements(By.XPATH, "//div[@class='a-section a-spacing-none']")

for check in tots:
   totalist.append(check.text)
print(totalist)
print("ttttttttt", len(totalist))

fiter = driver.find_elements(By.XPATH, "")
time.sleep(2)
driver.close()