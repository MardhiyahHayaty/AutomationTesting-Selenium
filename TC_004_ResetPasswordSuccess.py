from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

time.sleep(1)

link_forgot_pass = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p')
link_forgot_pass.click()

time.sleep(1)

username_field = driver.find_element(By.NAME, "username")
username_field.send_keys("Admin")

reset_button = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[2]')
reset_button.click()

time.sleep(2)
