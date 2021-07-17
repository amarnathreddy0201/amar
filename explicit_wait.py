from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="D:\Amarnath\drivers_chrome_ie_fire\chromedriver")
driver.get("https://selenium-python.readthedocs.io/waits.html")
try:
    element = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[7]/div/div[4]/div/div[1]/div/div[1]/div/div[4]/a"))
    )
finally:
    driver.quit()

#mine
"""import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver=webdriver.Chrome(executable_path="D:\Amarnath\drivers_chrome_ie_fire\chromedriver")
"""