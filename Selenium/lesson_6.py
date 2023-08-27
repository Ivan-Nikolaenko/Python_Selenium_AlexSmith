import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

user_name_1 = 'standard_user'
user_name_2 = 'locked_out_user'
user_name_3 = 'problem_user'
user_name_4 = 'performance_glitch_user'
password = 'secret_sauce'

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'

driver.get(base_url)
driver.maximize_window()
# user_name = driver.find_element(By.ID, "user-name") ID
# user_name = driver.find_element(By.NAME, "user-name") NAME
# user_name = driver.find_element(By.XPATH, '//*[@id="user-name"]') XPATH
# user_name = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input') FULL_XPATH
user_name = driver.find_element(By.ID, "user-name")
user_name.send_keys(user_name_2)
time.sleep(2)
driver.close()
