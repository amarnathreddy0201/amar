"""conditional commands"""
#is_displayed()
#is_enabled()
#is_selected()


import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="D:\Amarnath\drivers_chrome_ie_fire\chromedriver")
#driver=webdriver.Firefox(executable_path="D:\Amarnath\drivers_chrome_ie_fire\geckodriver")
driver.get("https://www.google.com/")
ele=driver.find_element_by_name("q")
ele.send_keys("facebook")
ele.submit()
#ele=driver.find_element_by_name("csi")
#ele.click()
#print(ele.is_displayed())

#print(ele.is_enabled())

driver.quit()
