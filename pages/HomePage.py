from selenium.webdriver.remote.webdriver import WebDriver



class HomePage:

    def __init__(self, driver: WebDriver):
         self.driver = driver
         self.__website_title = "Your Store"

    def is_page_visible(self, wishedValue: str):
        current_website_title = self.driver.title
        print(f"My current title is : {current_website_title}") 
        assert current_website_title == wishedValue
