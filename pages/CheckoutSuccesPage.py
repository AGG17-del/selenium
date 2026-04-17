from select import select

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

class CheckoutSuccessPage  (): 

     def __init__(self, driver: WebDriver):
         self.driver = driver
         self.revealed = '//h1'     
           
     def is_title_visible(self):
          revealed = self.driver.find_element(By.XPATH, self.revealed)
          return revealed.is_displayed()