import time
from time import sleep
from tkinter import Button

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v85.audits import disable
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://letcode.in/")
driver.maximize_window()
sleep(1)
driver.find_element(By.XPATH,'//a[normalize-space()="Explore Workspace"]').click()
sleep(1)
driver.find_element(By.PARTIAL_LINK_TEXT,"Cli").click()
sleep(2)
driver.find_element(By.XPATH,'//*[text()="Goto Home"]').click()
sleep(2)
driver.back()
sleep(2)
Location=driver.find_element(By.XPATH,'//*[text()="Find Location"]').location
print(Location)
Location1=driver.get_window_rect()
print(Location1)
Location2=driver.get_window_position()
print(Location2)
Location3=driver.get_window_size()
print(Location3)
color=driver.find_element(By.XPATH,'//*[text()="What is my color?"]').value_of_css_property("color")
print(color)
Size=driver.find_element(By.XPATH,'//*[text()="How tall & fat I am?"]').size
print(Size)
Disable=driver.find_element(By.XPATH,'//*[text()="Disabled"]').is_enabled()
print(Disable)
sleep(2)
button=driver.find_element(By.XPATH,'//*[text()="Button Hold!"]')
if button:
    # Create an ActionChains object
    actions = ActionChains(driver)

    # Perform the click and hold action
    actions.click_and_hold(button).perform()

    # Optionally, you can add a delay to observe the effect
    actions.pause(10)  # Pauses for 2 seconds while holding the button

    # Release the button
    actions.release(button).perform()
else:
    print("Button not found")
sleep(5)
driver.quit()





