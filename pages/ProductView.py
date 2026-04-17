from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class ProductView  (): 

    def __init__(self, driver: WebDriver):
         self.driver = driver
         self.btn_ViewCart = '//*[contains(text(),"View Cart")]'
              
    def clickON_btn_ViewCart(self):
        c_btn_ViewCart = self.driver.find_element(By.XPATH,self.btn_ViewCart)
        c_btn_ViewCart.click()    
    
    
