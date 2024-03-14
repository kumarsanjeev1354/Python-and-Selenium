print("hello test1")
from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com")
print("Application name is",driver.title)
print("Current url is",driver.current_url)
driver.quit()
print("URL Execution End")
