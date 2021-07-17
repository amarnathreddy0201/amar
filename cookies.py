import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="D:\Amarnath\drivers_chrome_ie_fire\chromedriver")

driver.get("https://www.amazon.in/")
print(driver.title)
"""
capture the all cookies
"""
cookies=driver.get_cookies()
print("len of cookies:",len(cookies))# how many cookies

print(cookies)# it will store in form of dictionary

driver.add_cookie({'name':'Amar','value':'sdvsd'})# adding cookie

cookies=driver.get_cookies()
print("len of cookies:",len(cookies))# how many cookies

print(cookies)



driver.delete_all_cookies()# Deleting cookies

cookies=driver.get_cookies()
print("len of cookies:",len(cookies))# how many cookies

print(cookies)

cookies=driver.get_cookie('domain')
#print("len of cookies:",len(cookies))# how many cookies

print(cookies)



"""
count noof cookies
adding cookies
deleting cookies
"""