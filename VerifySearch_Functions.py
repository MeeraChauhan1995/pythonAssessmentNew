import time
from selenium import webdriver
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

product_name = []

#search products by dropdown
driver.find_element(By.XPATH, './/span[@class="a-button-text a-declarative"]').click()
dropdowns = driver.find_elements(By.XPATH, '//li[@class="a-dropdown-item"]')

time.sleep(2)
for dropdown in dropdowns:
    print(dropdown.text)
    if dropdown.text == "Newest Arrivals":
        dropdown.click()
        time.sleep(2)
        break

driver.quit()
