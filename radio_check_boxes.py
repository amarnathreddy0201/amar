# PENDING
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="D:\Amarnath\drivers_chrome_ie_fire\chromedriver")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
print(driver.title)
#working with radio box

m=driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print("male statue:",m)
"""if m == "False":
e=driver.find_element_by_id("RESULT_RadioButton-7_0").click()


m=driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print("male statue:",m)"""



#check boxes
driver.find_element_by_name("RESULT_CheckBox-8").click()
s=driver.find_element_by_name("RESULT_CheckBox-8").is_selected()
print(s)


driver.find_element_by_id("RESULT_CheckBox-8_5").click()
s=driver.find_element_by_id("RESULT_CheckBox-8_5").is_selected()
print(s)





driver.quit()