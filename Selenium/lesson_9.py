import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

user_name_1 = 'standard_use'
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
user_name = driver.find_element(By.CSS_SELECTOR, "#user-name")
user_name.send_keys(user_name_1)
print("Input login")
user_pass = driver.find_element(By.ID, "password")
user_pass.send_keys(password)
print("Input password")
login_button = driver.find_element(By.XPATH, "//input[@type='submit']")
login_button.click()
print("Click login")
warring_text = driver.find_element(By.XPATH, "//h3[@data-test='error']")
value_warring_text = warring_text.text
assert value_warring_text == 'Epic sadface: Username and password do not match any user in this service'
print("Good test")
time.sleep(2)
driver.close()