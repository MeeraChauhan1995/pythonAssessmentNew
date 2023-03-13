import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service_obj = Service("C:/Meera/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service= service_obj)
driver.get("https://www.amazon.com/")

driver.implicitly_wait(5)

wait = WebDriverWait(driver, 10)  # explicit wait

driver.find_element(By.ID, 'nav-search-dropdown-card').click()

#potion 1 to search : search by dropdown
Droplist = Select(driver.find_element(By.XPATH, '//*[@id="searchDropdownBox"]'))
Droplist.select_by_visible_text("Books")
driver.find_element(By.ID, 'nav-search-submit-button').click()


##potion 2 to search : search by side nav bar
driver.find_element(By.XPATH, "//span[@class='hm-icon-label']").click()
driver.find_element(By.XPATH, "//ul[@class='hmenu hmenu-visible']")

#avail_ecategories= driver.find_elements(By.XPATH, "//a[@id='hmenu-content']")

avail_ecategories = wait.until(EC.presence_of_all_elements_located((By.ID, 'hmenu-content')))
print(avail_ecategories)

#to close nav bar
#driver.find_element(By.XPATH, "(//div[@class='nav-sprite hmenu-close-icon'])").click()

time.sleep(5)
for category in avail_ecategories:
    dept = category.find_element(By.XPATH, "//a[@class='hmenu-item']/div[contains(text(),'Electronics')]")
    print(category.text)
    if dept.text == "Electronics":
        dept.click()
        driver.find_element(By.LINK_TEXT, "Headphones").click()
        break

time.sleep(5)
driver.quit()