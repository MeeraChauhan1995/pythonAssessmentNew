import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service_obj = Service("C:/Meera/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service= service_obj)
driver.get("https://www.amazon.com/")

#enter item to search in search box
keyword = "hair dryer"
search = driver.find_element(By.XPATH, '//*[(@id = "twotabsearchtextbox")]')
search.send_keys(keyword)

# click search button
search_button = driver.find_element(By.ID, 'nav-search-submit-button')
search_button.click()

#apply filter by brand
driver.implicitly_wait(5)

brandlist = []

Brandnames = driver.find_elements(By.XPATH, "//span[@class='a-list-item']")
#Brandnames = driver.find_elements(By.ID, "brandsRefinements")

for brand in Brandnames:
       if brand.text == "Conair":
        brand.click()
        break
        print(brand.text)

#filter product by review
reviews = driver.find_elements(By.ID, "reviewsRefinements")
for review in reviews:
    #print(review.text)
    if review.find_element(By.XPATH, "//section[@aria-label='4 Stars & Up']"):
        print(review.find_element(By.XPATH, "//section[@aria-label='4 Stars & Up']").text)
        review.click()
        break

wait = WebDriverWait(driver, 10)  # explicit wait
totalitem = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='a-section a-spacing-base']")))

#final products after applying  all filters
for item in totalitem:
    productname = item.find_element(By.XPATH, "div/div/h2/a/span")
    if productname.text == "Conair Double Ceramic Hair Dryer, 1875W Hair Dryer with Ionic Conditioning":
        productname.click()
        break

driver.find_element(By.XPATH, "//*[@id='add-to-cart-button']").click()#addd to cart
errmsg= driver.find_element(By.XPATH, "//div[@class='a-fixed-left-grid-inner']").text

print(errmsg)
#check msg
assert "Added to Cart" in errmsg

driver.find_element(By.XPATH, "//*[@id='sw-gtc']").click()
subtotal =driver.find_element(By.XPATH, "//div[contains(@data-name,'Subtotals')]").text
print(subtotal)#print subtotal of item
assert subtotal

driver.find_element(By.ID, "sc-buy-box-ptc-button").click()

driver.find_element(By.XPATH,'//*[@id="ap_email"]').send_keys('+16476875247')

driver.find_element(By.ID, 'continue').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="ap_password"]').send_keys('Chauhan@1095')
driver.find_element(By.XPATH, '//*[@id="signInSubmit"]').click()


driver.quit()