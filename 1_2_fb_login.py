from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service

serv_obj=Service("C:\DRIVERS\chrome_driver\chromedriver.exe")

driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.facebook.com/")

abc=driver.find_element(By.NAME,'email')
abc.send_keys("rohit.adhav852@rediffmail.com")

pas=driver.find_element(By.XPATH,'//*[@id="pass"]')
pas.send_keys("rohit1234")

driver.find_element(By.NAME,'login').click()


driver.close()
