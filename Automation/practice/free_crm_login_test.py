import time

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def tes_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(15)
    driver.get('https://classic.freecrm.com/index.html')
    driver.maximize_window()
    username = driver.find_element(By.NAME, 'username')
    password = driver.find_element(By.NAME, 'password')
    username.send_keys('Arman')
    password.send_keys('Arman123')
    time.sleep(5)
    driver.refresh()
    time.sleep(5)
    try:
        username.send_keys('Arman')
        password.send_keys('Arman123')
    except StaleElementReferenceException:
        username = driver.find_element(By.NAME, 'username')
        password = driver.find_element(By.NAME, 'password')
        username.send_keys('Arman')
        password.send_keys('Arman123')
