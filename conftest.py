import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
@pytest.fixture(scope="class")
def setup(reuquest):
    service_obj = Service("C:/Meera/chromedriver_win32/chromedriver.exe")
    driver = webdriver.Chrome(service= service_obj)
    driver.get("https://www.amazon.com/")
    reuquest.cls.driver = driver
    yield
    driver.close()