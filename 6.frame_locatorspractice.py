import time
from faulthandler import is_enabled

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://letcode.in/frame")
driver.maximize_window()
driver.switch_to.frame(0)
driver.find_element(By.XPATH,"(//input[@type='text'])[1]").send_keys("Ajay")
driver.find_element(By.XPATH,"(//input[@type='text'])[2]").send_keys("Kumar")
time.sleep(3)
inner_frame = driver.find_element(By.XPATH,"//iframe[@src='innerframe']")
driver.switch_to.frame(inner_frame)
driver.find_element(By.XPATH,"(//input[@type='text'])[1]").send_keys("ajaygoud7991@yopmail.com")
time.sleep(3)
driver.switch_to.parent_frame()
fullname = driver.find_element(By.XPATH,"//p[@class='title has-text-info']")
print(fullname.text)
time.sleep(5)