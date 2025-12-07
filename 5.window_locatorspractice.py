from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://letcode.in/")
driver.maximize_window()
parent_handle=driver.current_window_handle
print(parent_handle)
sleep(1)
driver.find_element(By.XPATH,"//a[normalize-space()='Explore Workspace']").click()
sleep(1)
driver.find_element(By.XPATH,"//*[text()='Tabs']").click()
sleep(1)
driver.find_element(By.XPATH,"//button[@id='home']").click()
sleep(1)
All_handles=driver.window_handles
print(All_handles)
for handle in All_handles:
    if handle!=parent_handle:
        driver.switch_to.window(handle)
        sleep(3)
        title=driver.find_element(By.XPATH,"//h1").text
        print(title)
        break
driver.switch_to.window(parent_handle)
sleep(3)
parent_handle=driver.current_window_handle
print(parent_handle)
sleep(3)
driver.find_element(By.XPATH,"//*[@id='multi']").click()
sleep(3)
title=driver.find_element(By.XPATH,"//h1").text
print(title)
sleep(3)
driver.close()
sleep(3)
driver.quit()












