import time

from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

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

#fetch product list
items = wait(driver, 5).until(
    EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "s-result-item s-asin")]')))

for item in items:
    # find name
    name = item.find_element(By.XPATH, './/span[@class="a-size-medium a-color-base a-text-normal"]')
    product_name.append(name.text)
    break
print(product_name)
#using filter
driver.find_element(By.XPATH, './/span[@class="a-button-text a-declarative"]').click()
dropdowns = driver.find_elements(By.CLASS_NAME, 'a-popover-wrapper')
#dropdowns = driver.find_element(By.CLASS_NAME,"a-dropdown-link").get_attribute("value")

time.sleep(2)
for dropdown in dropdowns:
    print(dropdown.text)
    if dropdown.get_attribute('data-value') == "Newest Arrivals":
        dropdown.click()
        break

time.sleep(2)
driver.quit()
