import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver=webdriver.Chrome(executable_path="D:\Amarnath\drivers_chrome_ie_fire\chromedriver")
driver.get("https://www.bing.com/")

driver.implicitly_wait(300)

ele=driver.find_element_by_name("q")
ele.send_keys("cricket")
ele.submit()
#print(driver.implicitly_wait(100))


assert "cricket" in driver.title

driver.quit()