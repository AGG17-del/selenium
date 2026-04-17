from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class HeaderPageFragment(): 

    def __init__(self, driver: WebDriver):
         self.driver = driver
         self.menu = "//span[contains(text(),'Mega Menu')]"
         self.subMenu = '//*[contains(@title, "Power bank")]' 

    def select_menu(self):
        c_menu = self.driver.find_element(By.XPATH,self.menu)
        ActionChains(self.driver) \
        .move_to_element(c_menu) \
        .perform()
    
    def select_subMenu(self):
        c_subMenu = self.driver.find_element(By.XPATH,self.subMenu)
        c_subMenu.click()
            