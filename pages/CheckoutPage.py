from select import select

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

class CheckoutPage  (): 

     def __init__(self, driver: WebDriver):
         self.driver = driver
         self.lbl_SelectGuest = '//label[@for="input-account-guest"]'
         self.input_firstname = '//input[@name="firstname"]'
         self.input_lastname = '//input[@name="lastname"]'
         self.input_email = '//input[@name="email"]'
         self.input_telephone = '//input[@name="telephone"]'
         self.input_company = '//input[@name="company"]'
         self.input_adress_1 = '//input[@name="address_1"]'
         self.input_adress_2= '//input[@name="address_2"]'
         self.input_city = '//input[@name="city"]'
         self.input_postcode = '//input[@name="postcode"]'
         self.btn_country = '//*[@name="country_id"]'
         self.btn_selectCountry = '//*[@value="74"]/text()'
         self.btn_region = '//*[@name="zone_id"]'
         self.btn_selectRegion = '//*[@value="1143"]/text()'
         self.lbl_conditionTerms = '//label[@for="input-agree"]'
         self.btn_continue = '//button[@id="button-save"]'  
         self.btn_confirmOrder = '//*[@id="button-confirm"]'
         self.revealed = '//h1'


         
     def clickON_btn_CheckoutPPage(self):
        c_lbl_SelectGuest = self.driver.find_element(By.XPATH,self.lbl_SelectGuest)
        c_lbl_SelectGuest.click()    
            
     def sendkeys_firstname(self, wishedValue: str):
    
         firstname_input = self.driver.find_element(By.XPATH, self.input_firstname) 
         firstname_input.send_keys(wishedValue) 
    
     def sendkeys_lastname(self, wishedValue: str):
        
         lastname_input = self.driver.find_element(By.XPATH, self.input_lastname) 
         lastname_input.send_keys(wishedValue)
         
     def sendkeys_email(self, wishedValue: str):

         email_input = self.driver.find_element(By.XPATH, self.input_email) 
         email_input.send_keys(wishedValue)  
         
     def sendkeys_telephone(self, wishedValue: str):      
       
         telephone_input = self.driver.find_element(By.XPATH, self.input_telephone) 
         telephone_input.send_keys(wishedValue) 
         
     def sendkeys_company(self, wishedValue: str):      
         
         company_input = self.driver.find_element(By.XPATH, self.input_company) 
         company_input.send_keys(wishedValue)
     
     def sendkeys_adress_1(self, wishedValue: str):      
         
         adress_1_input = self.driver.find_element(By.XPATH, self.input_adress_1) 
         adress_1_input.send_keys(wishedValue) 
    
     def sendkeys_adress_2(self, wishedValue: str):      
         
         adress_2_input = self.driver.find_element(By.XPATH, self.input_adress_2) 
         adress_2_input.send_keys(wishedValue) 
    
     def sendkeys_city(self, wishedValue: str):      
         
         city_input = self.driver.find_element(By.XPATH, self.input_city) 
         city_input.send_keys(wishedValue) 
    
     def sendkeys_postcode(self, wishedValue: str):      
       
         postcode_input = self.driver.find_element(By.XPATH, self.input_postcode) 
         postcode_input.send_keys(wishedValue)     
    
     def select_btn_country(self, wishedValue: str ):
        select_element =self.driver.find_element(By.NAME, 'country_id')
        select_country = Select(select_element)
        select_country.select_by_visible_text(wishedValue)
           
     def select_btn_region(self, wishedValue: str):
        select_element =self.driver.find_element(By.NAME, 'zone_id')
        select_region = Select(select_element)
        select_region.select_by_visible_text(wishedValue)
    
     def clickON_lbl_conditionTerms(self):
        c_lbl_conditionTerms = self.driver.find_element(By.XPATH,self.lbl_conditionTerms)
        c_lbl_conditionTerms.click()   
        
     def clickON_btn_continue(self):
        c_btn_continue = self.driver.find_element(By.ID,"button-save")
        c_btn_continue.click()      
        
      
        
        
    