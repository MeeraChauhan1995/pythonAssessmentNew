import base64
import time
import urllib

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.utils import keys_to_typing

service_obj = Service("C:/Meera/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service= service_obj)
driver.get("https://www.amazon.com/")
action = ActionChains(driver)

driver.maximize_window()
#wait time to load web-elelements
driver.implicitly_wait(15)

Accountinfo = driver.find_element(By.ID, 'nav-link-accountList')
action.move_to_element(Accountinfo).perform()

driver.find_element(By.LINK_TEXT, 'Sign in').click()
#driver.find_element(By.XPATH,'//*[@id="ap_email"]').send_keys('+16476875247')

driver.find_element(By.XPATH,'//*[@id="ap_email"]').send_keys('meerachauhan67@gmail.com')
driver.find_element(By.ID, 'continue').click()

driver.find_element(By.XPATH, '//*[@id="ap_password"]').send_keys('Chauhan@1095')
driver.find_element(By.XPATH, '//*[@id="signInSubmit"]').click()

#password and emai correct then login successufully
#if not then below code will use
time.sleep(5)
alertmsg= driver.find_element(By.XPATH, '//*[@id="auth-warning-message-box"]').text
print(alertmsg)

driver.find_element(By.XPATH, '//*[@id="ap_password"]').send_keys('Chauhan@1095')

captacha =driver.find_element(By.XPATH, '//*[@id="auth-captcha-image"]')
src = captacha.get_attribute('src')

screenshot= driver.save_screenshot("captcha.png")
print(src)
print(screenshot)

driver.find_element(By.XPATH, '//*[@id="auth-captcha-guess"]').send_keys("C:/Users/ADMIN/PycharmProjects/pythonAssessment/captcha.png")
driver.find_element(By.XPATH, '//*[@id="signInSubmit"]').click()

#capture  error message
message = driver.find_element(By.XPATH, '//*[@id="auth-error-message-box"]').text


print(message)
driver.quit()