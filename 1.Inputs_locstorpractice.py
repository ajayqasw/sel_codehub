from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://letcode.in/")
driver.maximize_window()
sleep(5)
driver.find_element(By.XPATH,'//a[text()="Explore Workspace"]').click()
sleep(5)
driver.find_element(By.XPATH,"//a[text()='Edit']").click()
sleep(5)
driver.find_element(By.CSS_SELECTOR,"input#fullName").send_keys("Ajay Kumar")
sleep(2)
driver.find_element(By.XPATH,"//input[@id='join']").send_keys(" and what about you?" + Keys.TAB)
sleep(3)
attr_val=driver.find_element(By.XPATH,"//input[@id='getMe']").get_attribute("value")
print(attr_val)
sleep(3)
driver.find_element(By.XPATH,"//input[@id='clearMe']").clear()
sleep(3)
tet=driver.find_element(By.XPATH,"//input[@id='noEdit']").is_enabled()
print(tet)
test=driver.find_element(By.XPATH,"//input[@id='dontwrite']").get_attribute("value")
print(test)
sleep(3)

driver.quit()