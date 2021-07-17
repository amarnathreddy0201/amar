import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="D:\Amarnath\drivers_chrome_ie_fire\chromedriver")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
print(driver.title)

ele=driver.find_element_by_id("RESULT_RadioButton-9")
drp=Select(ele)

# 1)select by visible text
#drp.select_by_visible_text("Morning")

#2)select by index
    #1 null,2 morning , 3 AAfter noon,4 evening
#drp.select_by_index(2)

#3) select by value
drp.select_by_value("Radio-1")

#count noof options

print(len(drp.options))

#capture the all options
all_options=drp.options
j=1
for i in all_options:
    print(j,")",i.text)
    j+=1


