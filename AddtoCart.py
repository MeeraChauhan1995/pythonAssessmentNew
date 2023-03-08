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
time.sleep(3)

mainpage =driver.find_element(By, 'div.sg-col-20-of-24' )
listofproducts = mainpage.find_elements(By.CLASS_NAME, 'a-size-base-plus a-color-base a-text-normal')
for item in listofproducts:
 try:
  item.find_element(By.CSS_SELECTOR, 'div.a-row')
  ans = True
 except:
  ans = False
  if (ans):
   item.find_element(By.CSS_SELECTOR, 'span.a-size-medium').click()
   break

#driver.switch_to.window(driver.window_handles[1]) #rused to switche between

addtocart = driver.find_element(By.XPATH, '//*[@id="add-to-cart-button"]')
addtocart.click()
time.sleep(3)
proceed = driver.find_element(By.XPATH, '//*[(@id = "hlb-otc-btn-native]"]')
proceed.click()
time.sleep(3)
driver.close()