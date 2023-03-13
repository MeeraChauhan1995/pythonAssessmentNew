import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Meera/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service= service_obj)
driver.get("https://www.amazon.com/")

action = ActionChains(driver)

#maximize the window
driver.maximize_window()

Accountinfo = driver.find_element(By.ID, 'nav-link-accountList')

#mouse over to account information to sign in
action.move_to_element(Accountinfo).perform()

#wait time to load web-elelements
driver.implicitly_wait(5)

#new user registration testing
print("new user")

driver.find_element(By.XPATH, '//*[@id="nav-flyout-ya-newCust"]/a').click()
driver.find_element(By.ID, 'ap_customer_name').send_keys('Meera Chauhan')

#driver.find_element(By.ID, 'ap_email').send_keys('6476875247')
driver.find_element(By.ID, 'ap_email').send_keys('mrc6467@gmail.com')


driver.find_element(By.ID, 'ap_password').send_keys('chauhan@1095')

driver.find_element(By.ID, 'ap_password_check').send_keys('chauhan@1095')

# click on verify mobile number
driver.find_element(By.ID, 'continue').click()

#capture  error message using phone number
#errmessage = driver.find_element(By.XPATH, '//*[@id="auth-error-message-box"]').text

#iframe
driver.find_element(By.XPATH, "@id = cvf-aamation-challenge-iframe")
time.sleep(20)
#capture  error message using email id
message = driver.find_element(By.XPATH, '//*[@class="a-box a-alert a-alert-warning a-spacing-base"]').text

#print(errmessage)

print(message)
assert "Successfully" in message
driver.quit()
