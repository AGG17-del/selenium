from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class Checkout  (): 

    def __init__(self, driver: WebDriver):
         self.driver = driver
         self.btn_Checkout = '//*[contains(text(),"Checkout")]'
              
    def clickON_btn_Checkout(self):
        c_btn_Checkout = self.driver.find_element(By.XPATH,self.btn_Checkout)
        c_btn_Checkout.click()    
    
    
