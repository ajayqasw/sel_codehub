from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v85.audits import disable
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://letcode.in/")
driver.maximize_window()
sleep(5)
driver.find_element(By.XPATH,"//a[normalize-space()='Explore Workspace']").click()
sleep(3)
driver.find_element(By.XPATH,"//*[text()='Toggle']").click()
sleep(3)
driver.find_element(By.XPATH,"//input[@id='yes']").click()
sleep(3)
t1=driver.find_element(By.XPATH,"//input[@id='two']").is_selected()
print(t1)
sleep(3)
driver.find_element(By.XPATH,"//input[@id='nobug']").click()
sleep(3)
driver.find_element(By.XPATH,"//input[@id='bug']").click()
sleep(3)
text=driver.find_element(By.XPATH,"//input[@id='notfoo']").text
print(text)
sleep(3)
t2=driver.find_element(By.XPATH,"//input[@id='maybe']").is_enabled()
print(t2)
sleep(3)
t3=driver.find_element(By.XPATH,"//label[normalize-space()='Remember me']").is_displayed()
print(t3)
sleep(3)

driver.find_element(By.XPATH,"(//input[@type='checkbox'])[2]").click()
sleep(3)

