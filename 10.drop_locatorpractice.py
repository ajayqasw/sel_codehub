from time import sleep

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

class DropLocatorPractice:
    def drop_locator_practice(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://letcode.in/")
        driver.maximize_window()
        driver.find_element(By.LINK_TEXT, "Explore Workspace").click()
        element = driver.find_element(By.LINK_TEXT, "AUI - 2")
        driver.execute_script("arguments[0].click();", element)
        source = driver.find_element(By.XPATH, "//div[@id='draggable']")
        target = driver.find_element(By.XPATH, "//div[@id='droppable']")
        action = ActionChains(driver)
        action.drag_and_drop(source, target).perform()
        sleep(5)
        driver.quit()
dd=DropLocatorPractice()
dd.drop_locator_practice()
