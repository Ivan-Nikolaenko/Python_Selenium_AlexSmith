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
user_name = driver.find_element(By.ID, "user-name")
user_name.click()
user_name.send_keys(user_name_1)
user_pass = driver.find_element(By.ID, "password")
user_pass.click()
user_pass.send_keys(password)
login_button = driver.find_element(By.ID, "login-button")
login_button.click()
time.sleep(2.5)


driver.close()