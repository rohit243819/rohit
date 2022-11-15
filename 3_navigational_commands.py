from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\DRIVERS\chrome_driver\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)


driver.get("https://www.snapdeal.com/")
driver.maximize_window()
driver.get("https://www.amazon.com/")
driver.minimize_window()


driver.back()
driver.forward()
driver.refresh()


# driver.quit()