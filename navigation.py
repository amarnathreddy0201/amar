#Navigation moving forward and backward

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox(executable_path="D:\Amarnath\drivers_chrome_ie_fire\geckodriver")
#driver=webdriver.Chrome(executable_path="D:\Amarnath\drivers_chrome_ie_fire\chromedriver")
driver.get("https://www.google.com/search?q=movies/")
print(driver.title)
time.sleep(2)
driver.get("https://www.google.com/search?q=cricket/")
print(driver.title)
time.sleep(2)
driver.back()
print(driver.title)
time.sleep(2)
driver.forward()
print(driver.title)


time.sleep(2)

driver.close()
