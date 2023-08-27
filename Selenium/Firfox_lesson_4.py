import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service(r'C:\Users\admin\PycharmProjects\AlexSmithSelenium\chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.get('https://www.saucedemo.com/')
time.sleep(3)
driver.maximize_window()
driver.close()