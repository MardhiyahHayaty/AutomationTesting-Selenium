from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
driver.maximize_window()

time.sleep(1)

username_field = driver.find_element(By.NAME, "username")
password_field = driver.find_element(By.NAME, "password")
login_button = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')

username_field.send_keys("Admin")
password_field.send_keys("admin123")
login_button.click()

time.sleep(2)

PIM_menu = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
PIM_menu.click()

time.sleep(1)

add_emp = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]')
add_emp.click()

time.sleep(3)

firstname_emp = driver.find_element(By.NAME, "firstName")
firstname_emp.send_keys("Putri")

middlename_emp = driver.find_element(By.NAME, "middleName")
middlename_emp.send_keys("Anjani")

lastname_emp = driver.find_element(By.NAME, "lastName")
lastname_emp.send_keys("Sinta")

time.sleep(3)

save_emp = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')
save_emp.click()

time.sleep(1)