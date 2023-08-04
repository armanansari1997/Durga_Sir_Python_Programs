import time
import logging

from behave import *
# from pyparsing import And
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@given('User is on Payment screen')
def impl_bkpy(context):
    global logger
    logger = logging.getLogger()
    logger.info("Context : User is on Payment screen")
    # print('User is on Payment screen')
    # print("context: " , context)
    options = Options()
    # options.add_argument('start-maximized')
    # options.add_argument('headless')
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


@when('User clicks on Payment types')
def impl_bkpy(context):
    # print('User clicks on Payment types')
    logger.info('Context : User clicks on Payment types')
    # print("context: " , context)
    # print('UserPaymentTypes')
    driver.get('https://www.google.com')
    title = driver.title
    driver.maximize_window();
    logger.info(title)
    time.sleep(2)


@then('User should get Types Cheque and Cash')
def impl_bkpy(context):
    # print('Hello user should get Types Cheque and Cash')
    logger.info("context: User should get Types Cheque and Cash")
    # print('Cash')
    search = driver.find_element(By.NAME, 'q')
    search.send_keys('python.org')
    search.submit()
    logger.info(driver.title)
    time.sleep(2)
    driver.close()
