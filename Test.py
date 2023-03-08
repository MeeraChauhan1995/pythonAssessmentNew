from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

service_obj = Service("C:/Meera/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service= service_obj)
driver.get("https://www.amazon.com/")

driver.implicitly_wait(5)
keyword = "Airtags"
search = driver.find_element(By.XPATH,'//*[(@id = "twotabsearchtextbox")]')
search.send_keys(keyword)
# click search button
search_button = driver.find_element(By.ID, 'nav-search-submit-button')
search_button.click()

driver.implicitly_wait(5)


product_name = []
product_price = []
best_seller = []

items = wait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "s-result-item s-asin")]')))
for item in items:
    # find name
    name = item.find_element(By.XPATH, './/span[@class="a-size-medium a-color-base a-text-normal"]')
    product_name.index(0)
    product_name.append(name.text)

#name == 'bestseller'
sell = item.find_elements(By.XPATH,'.//span[@class="rush-component"]')

driver.quit()

# to check data scraped
print(product_name)
#print(product_asin)
