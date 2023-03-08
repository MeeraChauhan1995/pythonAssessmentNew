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

Deliverto = driver.find_element(By.ID, 'nav-global-location-popover-link')

#mouse over to account information to sign in
action.move_to_element(Deliverto).perform()

#wait time to load web-elelements
driver.implicitly_wait(3)
myalert= driver.find_element(By.XPATH, '//div[@role="alertdialog"]').text
print(myalert)

#for alert in myalert:
 #   driver.find_element(By.XPATH, '//span[@class="a-button-inner"])[1]').click()


#myalert = driver.switch_to.alert
#myalert.dismiss()
#myalert.accept()
driver.close()