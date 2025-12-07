from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://letcode.in/")
driver.maximize_window()
title = driver.title
print(title)
driver.find_element(By.XPATH,'//a[normalize-space()="Explore Workspace"]').click()
sleep(1)
driver.find_element(By.XPATH,"//*[text()='Dialog']").click()
sleep(1)
driver.find_element(By.XPATH,'//*[@id="accept"]').click()
sleep(1)
driver.switch_to.alert.accept()
sleep(1)
driver.find_element(By.XPATH,'//*[@id="confirm"]').click()
sleep(1)
driver.switch_to.alert.dismiss()
sleep(1)
driver.find_element(By.XPATH,'//*[text()="Prompt Alert"]').click()
sleep(1)
driver.switch_to.alert.send_keys("Ajay Kumar")
sleep(1)
driver.switch_to.alert.accept()
sleep(1)
driver.find_element(By.XPATH,'//*[text()="Modern Alert"]').click()
sleep(5)
driver.find_element(By.XPATH,'//*[@aria-label="close"]').click()
sleep(5)







