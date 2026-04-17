from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class ProductListPage(): 

    def __init__(self, driver: WebDriver):
         self.driver = driver
         self.lbl_availablityFilter = '(//*[contains(text(), "In stock")])[2]/..'
         self.productItem = '(//*[@class= "carousel-item active"]/*[@class= "lazy-load"])[3]'

    def clickOn_FilterOnStock(self):
        c_lbl_availablityFilter = self.driver.find_element(By.XPATH,self.lbl_availablityFilter)
        c_lbl_availablityFilter.click()
        
    
    def select_ProductItem(self):
        c_productItem = self.driver.find_element(By.XPATH,self.productItem)
        c_productItem.click()
