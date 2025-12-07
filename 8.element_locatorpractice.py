from time import sleep

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class ElementLocatorPractice():
    def demoelements(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://letcode.in/")
        driver.maximize_window()
        sleep(2)
        element = driver.find_element(By.XPATH, "//a[normalize-space()='Explore Workspace']")
        driver.execute_script("arguments[0].click();", element)
        sleep(2)
        element1=driver.find_element(By.XPATH, "//a[text()='Find Elements']")
        driver.execute_script("arguments[0].click();", element1)
        sleep(2)
        driver.find_element(By.XPATH, "//*[@type='text']").send_keys("Ajaygowda2197")
        sleep(2)
        driver.find_element(By.XPATH, "//*[@type='text']").click()
        sleep(2)

        try:
            image_element = driver.find_element(By.XPATH, "//img[@alt='Placeholder image']")
            print("Image is present")
        except NoSuchElementException:
            print("Image is not present")


demostate = ElementLocatorPractice()
demostate.demoelements()
