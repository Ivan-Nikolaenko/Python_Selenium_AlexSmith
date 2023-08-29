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
user_name = driver.find_element(By.CSS_SELECTOR, "#user-name")
user_name.send_keys(user_name_1)
print("Input login")
user_pass = driver.find_element(By.ID, "password")
user_pass.send_keys(password)
print("Input password")
login_button = driver.find_element(By.XPATH, "//input[@type='submit']")
login_button.click()
print("Click login")
# text_products = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
# value_text_products = text_products.text
# assert value_text_products == "PRODUCTS"
# print("Assert title")
# time.sleep(2)
# driver.close()

URL = "https://www.saucedemo.com/inventory.html"
get_url = driver.current_url
assert URL == get_url
print("URL OK")
