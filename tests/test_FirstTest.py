import sys
import os
import pytest
from pageFragments.HeaderPageFragment import HeaderPageFragment
from pages.HomePage import HomePage 
from helpers.BaseTest import BaseTest
from time import sleep
from pages.ProductListePage import ProductListPage
from pages.ProductPage import ProductPage   
from pages.ProductView import ProductView
from pages.Checkout import Checkout
from pages.CheckoutPage import CheckoutPage
from selenium.webdriver.support import expected_conditions 
from pages.CheckoutConfirmPage import CheckoutConfirmPage
from pages.CheckoutSuccesPage import CheckoutSuccessPage
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..")) 



class Test_FirstTest(BaseTest): 

    @pytest.mark.test_MyFirstTest
    def test_MyFirstTest(self):
        self.open_application()
        
        home = HomePage(self.driver) 
        home.is_page_visible("Your Store")
        
        header = HeaderPageFragment(self.driver)
        header.select_menu()
        header.select_subMenu()
        
        productList = ProductListPage(self.driver)
        productList.clickOn_FilterOnStock()
        sleep(3)
        productList.select_ProductItem()
        
        add_item = ProductPage(self.driver)
        add_item.clickON_btn_AddToCart()
        
        add_item = ProductView(self.driver)
        add_item.clickON_btn_ViewCart() 
        
        checkout = Checkout(self.driver)
        checkout.clickON_btn_Checkout() 
        
        checkoutPage = CheckoutPage(self.driver)
        checkoutPage.clickON_btn_CheckoutPPage() 
        
        checkoutPage.sendkeys_firstname("John")
        checkoutPage.sendkeys_lastname("Doe")
        checkoutPage.sendkeys_email("john.doe@example.com")
        checkoutPage.sendkeys_telephone("0421234567")
        checkoutPage.sendkeys_company("ABC Company")
        checkoutPage.sendkeys_adress_1("123 Main Street")
        checkoutPage.sendkeys_adress_2("Apartment 456")
        checkoutPage.sendkeys_city("Lamballe")
        checkoutPage.sendkeys_postcode("44001")
        checkoutPage.select_btn_country("France, Metropolitan")
        checkoutPage.select_btn_region("Finistère")
        checkoutPage.clickON_lbl_conditionTerms()
        sleep(2)
        
        checkoutPage.clickON_btn_continue()
        checkoutConfirmPage = CheckoutConfirmPage(self.driver)
        checkoutConfirmPage.clickON_btn_confirmOrder()
        
        sleep(2)
        checkoutSuccessPage = CheckoutSuccessPage(self.driver)
        assert checkoutSuccessPage.is_title_visible() == True
        print(f"Votre commande a été confirmée avec succès !")
        