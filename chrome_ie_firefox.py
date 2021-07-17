from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver=webdriver.Firefox(executable_path="D:\Amarnath\drivers_chrome_ie_fire\geckodriver")
driver=webdriver.Ie(executable_path="D:\Amarnath\drivers_chrome_ie_fire\IEDriverServer")
#driver=webdriver.Chrome(executable_path="D:\Amarnath\drivers_chrome_ie_fire\chromedriver")
driver.get("https://www.youtube.com/")#IEDriverServer
print(driver.title)
print(driver.current_url)
print(driver.page_source)
driver.close()