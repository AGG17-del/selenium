from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class ProductPage  (): 

    def __init__(self, driver: WebDriver):
         self.driver = driver
         self.btn_AddToCart = '(//button[contains(text(),"Add to Cart")])[2]'
         self.btn_ViewCart = '//*[contains(text(),"View Cart")]'
         


    def clickON_btn_AddToCart(self):
        c_btn_AddToCart = self.driver.find_element(By.XPATH,self.btn_AddToCart)
        c_btn_AddToCart.click()
        
        
    def clickON_btn_ViewCart(self):
        c_btn_ViewCart = self.driver.find_element(By.XPATH,self.btn_ViewCart)
        c_btn_ViewCart.click()    
    
    
