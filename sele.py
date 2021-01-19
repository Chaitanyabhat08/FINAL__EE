from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
driver.get("https://studentmanagementsystem8.herokuapp.com/admin_home")
print(driver.title)
print(driver.page_source)
driver.close()