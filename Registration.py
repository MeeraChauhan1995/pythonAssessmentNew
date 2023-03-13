import time

import pytest
import self as self
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class TestOne:
    def Test_Regsitration(self, setup):
        action = ActionChains(self.driver)
        #maximize the window
        self.driver.maximize_window()
        Accountinfo = self.driver.find_element(By.ID, 'nav-link-accountList')
        #mouse over to account information to sign in
        action.move_to_element(Accountinfo).perform()
        #wait time to load web-elelements
        self.driver.implicitly_wait(5)
        #new user registration testing
        print("new user")

        self.driver.find_element(By.XPATH, '//*[@id="nav-flyout-ya-newCust"]/a').click()
        self.driver.find_element(By.ID, 'ap_customer_name').send_keys('Meera Chauhan')

        #driver.find_element(By.ID, 'ap_email').send_keys('6476875247')
        self.driver.find_element(By.ID, 'ap_email').send_keys('mrc6467@gmail.com')


        self.driver.find_element(By.ID, 'ap_password').send_keys('chauhan@1095')

        self.driver.find_element(By.ID, 'ap_password_check').send_keys('chauhan@1095')

        #click on verify mobile number
        self.driver.find_element(By.ID, 'continue').click()

        #capture  error message using phone number
        #errmessage = driver.find_element(By.XPATH, '//*[@id="auth-error-message-box"]').text

        #iframe
        self.driver.find_element(By.XPATH, "@id = cvf-aamation-challenge-iframe")
        time.sleep(20)
        #capture  error message using email id
        message = self.driver.find_element(By.XPATH, '//*[@class="a-box a-alert a-alert-warning a-spacing-base"]').text

        #print(errmessage)

        print(message)
        assert "Successfully" in message
