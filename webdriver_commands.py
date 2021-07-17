import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver=webdriver.Chrome(executable_path="D:\Amarnath\drivers_chrome_ie_fire\chromedriver")

driver.get("https://www.bing.com/")


print(driver.title)
print(driver.current_url)
print(driver.page_source)

driver.find_element_by_id("sb_form").click()
driver.find_element_by_id("sb_form_q").send_keys("amar reddy")
time.sleep(5)
driver.quit()