import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="D:\Amarnath\drivers_chrome_ie_fire\chromedriver")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
#input box

#how to find how many inboxes present in web page
#how to provide value into text box
#how to get the status

inputboxes=driver.find_elements(By.CLASS_NAME , "text_field")
print(len(inputboxes))

#status
status=driver.find_element(By.ID,"RESULT_TextField-1").is_displayed()
print("element 1 display",status)

status=driver.find_element(By.ID,"RESULT_TextField-1").is_enabled()
print("element 1 enabled",status)

status=driver.find_element(By.ID,"RESULT_TextField-2").is_displayed()
print("status 2 displayed",status)

status=driver.find_element(By.ID,"RESULT_TextField-2").is_enabled()
print("status 2 displayed",status)

status=driver.find_element(By.ID,"RESULT_TextField-3").is_displayed()
print("status 3 displayed",status)

status=driver.find_element(By.ID,"RESULT_TextField-3").is_enabled()
print("status 3 enabled",status)

#value into the box
driver.find_element(By.ID,"RESULT_TextField-1").send_keys("Amar")

driver.find_element(By.ID,"RESULT_TextField-2").send_keys("Reddy")

driver.find_element(By.ID,"RESULT_TextField-3").send_keys("9494225071")


time.sleep(2)

driver.quit()