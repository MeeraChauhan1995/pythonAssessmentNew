import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import re

service_obj = Service("C:/Meera/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service= service_obj)
driver.get("https://www.amazon.com/")

driver.implicitly_wait(5)

driver.find_element(By.ID, 'nav-cart-count').click()
errmsg= driver.find_element(By.ID, 'sc-active-cart').text
print(errmsg)

buttons = driver.find_elements(By.XPATH, "//a[@class='a-button-text']")

for button in buttons:
    if button.text == "Sign in to your account":
        button.click()
        break

driver.find_element(By.ID, "ap_email").send_keys("+16476875247")
driver.find_element(By.ID, "continue").click()

driver.find_element(By.ID, "ap_password").send_keys("Chauhan@1095")
driver.find_element(By.ID, "signInSubmit").click()

products = driver.find_elements(By.XPATH, "//div[@class='sc-list-item-content']")
print(products)

# for product in products:
#     product.find_element(By.XPATH, "//input[@value='Save for later']").click()

totalprice = driver.find_elements(By.XPATH, "//div[@class='sc-item-price-block']")
print(totalprice)

#add product prices and compare
value = ""
sum = 0.0
for price in totalprice:
    value = price.text.strip('$')
    sum = sum + float(value)
    print(sum)

subtotal = float(driver.find_element(By.ID, "sc-subtotal-amount-activecart").text.strip(' $'))
print(subtotal)
time.sleep(3)

assert sum == subtotal # test will pass if both values match

#select or deletect item from the lsit
#driver.find_element(By.XPATH, "//div[@class='a-checkbox a-checkbox-fancy sc-item-check-checkbox-pc-desktop sc-list-item-checkbox']").click()

driver.close()
