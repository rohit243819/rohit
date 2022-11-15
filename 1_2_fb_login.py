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


driver.find_element(By.XPATH,'//*[@id="mount_0_0_QS"]/div/div[1]/div/div[2]/div[3]/div[1]/span/div/div[1]/div/svg/g/image').click()
driver.back()



#driver.find_element(By.NAME,"txtUsername").send_keys("Admin")
#
# driver.find_element(By.NAME,"identifire").send_keys("Admin")
#
# #driver.find_element(by.name= By.id)
#

'''
driver.find_element(By.ID,"txtPassword").send_key("admin123")
driver.find_element(By.ID,"btnLogin").click()


act_title=driver.title
exp_title="OrangeHRM"

if act_title==exp_title:
    print("Login test passed")
else:
    print("Login is failed")
driver.close()



from selenium import webdriver
from selenium.webdriver.common.by import By


from selenium.webdriver.chrome.service import Service

serv_obj=Service("C:\DRIVERS\chrome_driver\chromedriver.exe")

driver=webdriver.Chrome(service=serv_obj)

driver.get("https://accounts.google.com/")



driver.find_element(By.NAME,"identifier").send_keys("rohit.adhav852@gmail.com")
driver.find_element(By.XPATH,"//*[@id='identifierNext']/div/button/span").click()

# //*[@id="passwordNext"]/div/button
# driver.find_element(By.ID,"txtPassword").send_key("admin123")
# driver.find_element(By.ID,"btnLogin").click()
#
#
# act_title=driver.title
# exp_title="OrangeHRM"
#
# if act_title==exp_title:
#     print("Login test passed")
# else:
#     print("Login is failed")
# driver.close()
# '''



'''
Gmail login

import time 

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service

serv_obj=Service("C:\DRIVERS\chrome_driver\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://accounts.google.com/signup")
driver.maximize_window()

driver.find_element(By.NAME,"firstName").send_keys("rohit")
driver.find_element(By.NAME,"lastName").send_keys("adhav")
driver.find_element(By.NAME,"Username").send_keys("rohit.adhav852")

driver.find_element(By.NAME,"Passwd").send_keys("rohit1234")
driver.find_element(By.NAME,"ConfirmPasswd").send_keys("rohit1234")

driver.find_element(By.XPATH,"//input[@type='checkbox']").click()

driver.find_element(By.XPATH,"//span[normalize-space()='Next']").click()

time.sleep(2)

driver.find_element(By.XPATH,"//span[normalize-space()='Sign in instead']").click()

time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='identifierId']").send_keys("rohit.adhav852@gmail.com")

driver.find_element(By.XPATH,"//span[normalize-space()='Next']").click()

time.sleep(2)
driver.find_element(By.NAME,"password").send_keys("12345754")

time.sleep(2)
driver.find_element(By.XPATH,"//span[normalize-space()='Next']").click()


'''