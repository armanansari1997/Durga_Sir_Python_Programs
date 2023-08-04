import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def load_the_driver_using_service_object():
    options = Options()
    # options.add_argument('start-maximized')
    options.add_argument('headless')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get('https://www.google.com')
    title = driver.title
    driver.maximize_window();
    print(title)
    time.sleep(2)
    search = driver.find_element(By.NAME, 'q')
    search.send_keys('python.org')
    search.submit()
    time.sleep(2)


if __name__ == '__main__':
    load_the_driver_using_service_object()
