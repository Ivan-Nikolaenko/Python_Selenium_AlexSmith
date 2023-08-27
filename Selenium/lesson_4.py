import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# более простой вариант
# driver = webdriver.Chrome()
# base_url = 'https://www.saucedemo.com/'
# driver.get(base_url)
# driver.quit()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()
time.sleep(1)
driver.close()
