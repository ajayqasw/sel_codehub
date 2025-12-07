from statistics import multimode

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://letcode.in/")
driver.maximize_window()
sleep(1)
driver.find_element(By.XPATH,'//a[normalize-space()="Explore Workspace"]').click()
sleep(1)
driver.find_element(By.XPATH,'//*[text()="Drop-Down"]').click()
sleep(1)
select= driver.find_element(By.XPATH, '//*[@id="fruits"]')
dropdown=Select(select)
dropdown.select_by_visible_text("Apple")
sleep(2)
dropdown.select_by_index(2)
sleep(2)
dropdown.select_by_value("2")
sleep(2)
select_element=driver.find_element(By.XPATH,'//*[@id="superheros"]')
select=Select(select_element)
select.select_by_value("am")
select.select_by_visible_text("Aquaman")
select.select_by_index()
select.deselect_all()
sleep(2)
selected_options=select.all_selected_options
for option in selected_options:
  print(option.text)
sleep(2)
driver.quit()






