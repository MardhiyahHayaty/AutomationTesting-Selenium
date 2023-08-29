from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.techwithtim.net/")
time.sleep(10)


##options = webdriver.EdgeOptions()
##options.add_experimental_option('detach', True)

##driver = webdriver.Edge(options=options)
##driver.get("https://www.techwithtim.net/")