import time
import pytesseract as pytesseract
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pytesseract import image_to_string
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:/Meera/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service= service_obj)
driver.get("https://www.amazon.com/")
action = ActionChains(driver)

driver.maximize_window()
#wait time to load web-elelements
driver.implicitly_wait(15)
#mousehover function perform
Accountinfo = driver.find_element(By.ID, 'nav-link-accountList')
action.move_to_element(Accountinfo).perform()

#Case1: password and email correct then login successufully

driver.find_element(By.LINK_TEXT, 'Sign in').click()
driver.find_element(By.XPATH,'//*[@id="ap_email"]').send_keys('+16476875247')

#driver.find_element(By.XPATH,'//*[@id="ap_email"]').send_keys('meerachauhan67@gmail.com')
driver.find_element(By.ID, 'continue').click()

driver.find_element(By.XPATH, '//*[@id="ap_password"]').send_keys('Chauhan@1095')#using Correct passowrd
driver.find_element(By.XPATH, '//*[@id="ap_password"]').send_keys('Chauhan@105')#using Incorrect passowrd

driver.find_element(By.XPATH, '//*[@id="signInSubmit"]').click()

# case:2 if not then below code will use
time.sleep(2)
alertmsg= driver.find_element(By.XPATH, '//*[@id="auth-warning-message-box"]').text
print(alertmsg)

driver.find_element(By.XPATH, '//*[@id="ap_password"]').send_keys('Chauhan@1095')


#using tesseract, take screenshot, read text from screenshot
path_to_tesseract = r"C:/Program Files (x86)/Tesseract-OCR/tesseract.exe"
captacha =driver.find_element(By.XPATH, '//*[@id="auth-captcha-image"]')
captacha.screenshot('captcha.png')
src = captacha.get_attribute('src')
print(src)

#convert image to string
imgpath = r"C:/Users/ADMIN/PycharmProjects/pythonAssessment/captcha.png"
img = Image.open(imgpath)
pytesseract.tesseract_cmd = path_to_tesseract
#data= pytesseract.image_to_osd(img)
#print(data)

time.sleep(2)

#driver.find_element(By.XPATH, '//*[@id="auth-captcha-guess"]').send_keys(data)
driver.find_element(By.XPATH, '//*[@id="auth-captcha-guess"]').send_keys(src)

driver.find_element(By.XPATH, '//*[@id="signInSubmit"]').click()

#capture  error message
message = driver.find_element(By.XPATH, '//*[@id="auth-error-message-box"]').text


print(message)
driver.quit()