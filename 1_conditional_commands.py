from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj=Service("C:\DRIVERS\chrome_driver\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)


driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()


#is displayed   isenabled

searchbox=driver.find_element(By.XPATH,"//*[@id='small-searchterms']")

print("Display status:",searchbox.is_displayed())
print("Display status:",searchbox.is_enabled())

rd_male=driver.find_element(By.XPATH,"//*[@id='gender-male']")
rd_female=driver.find_element(By.XPATH,"//*[@id='gender-female']")

print(rd_male.is_selected())
print(rd_female.is_selected())

rd_male.click()


print("after selecting button")
print(rd_male.is_selected())
print(rd_female.is_selected())

# rd_female.click()
# print("after selecting button")
# print(rd_male.is_selected())
# print(rd_female.is_selected())


driver.find_element(By.NAME,"FirstName").send_keys("Rohit")
driver.find_element(By.NAME,"LastName").send_keys("Adhav")


driver.find_element(By.NAME,"DateOfBirthDay").send_keys("15")
driver.find_element(By.NAME,"DateOfBirthMonth").send_keys("January")
driver.find_element(By.NAME,"DateOfBirthYear").send_keys("1995")
driver.find_element(By.NAME,"Email").send_keys("rohit.adhav852@gmail.com")
driver.find_element(By.NAME,"Company").send_keys("sigma")

driver.find_element(By.NAME,"Newsletter").click()

driver.find_element(By.NAME,"Password").send_keys("rohit1234")

driver.find_element(By.NAME,"ConfirmPassword").send_keys("rohit1234")



driver.find_element(By.NAME,"register-button").click()

print("account created successfully")




#print("Display status",searchbox.is_selected())


#driver.quit()

