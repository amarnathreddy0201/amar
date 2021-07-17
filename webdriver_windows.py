import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="D:\Amarnath\drivers_chrome_ie_fire\chromedriver")

driver.get("http://demo.automationtesting.in/Windows.html")
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
#print(driver.current_window_handle) #PARENT WINDOW


#driver.current_window_handle
handles=driver.window_handles     #all windows values
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title == "Frames & windows":
        driver.close()


#driver.quit()    #cleare the all windows







#driver.window_handle