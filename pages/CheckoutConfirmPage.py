from select import select
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

class CheckoutConfirmPage  (): 

     def __init__(self, driver: WebDriver):
         self.driver = driver   
         self.btn_confirmOrder = '//*[@id="button-confirm"]'
        

     def clickON_btn_confirmOrder(self):
        c_btn_confirmOrder = self.driver.find_element(By.XPATH, self.btn_confirmOrder)
        c_btn_confirmOrder.click()       
        
        
  