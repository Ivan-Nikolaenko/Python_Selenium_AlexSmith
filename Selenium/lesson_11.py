import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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
user_pass = driver.find_element(By.ID, "password")
user_pass.send_keys(password)
print("Input password")
user_pass.send_keys(Keys.ENTER)
# drop_down_menu = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select')
drop_down_menu = driver.find_element(By.XPATH, "//select[@data-test='product_sort_container']")
drop_down_menu.click()
time.sleep(2)
drop_down_menu.send_keys(Keys.ARROW_DOWN*2)
drop_down_menu.send_keys(Keys.ARROW_UP*1)
drop_down_menu.send_keys(Keys.ENTER)

