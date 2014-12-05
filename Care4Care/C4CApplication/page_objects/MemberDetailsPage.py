from C4CApplication.page_objects.FixedPage import FixedPage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


import time


class MemberDetailsPage(FixedPage): 
    def __init__(self, driver):
        super().__init__(driver)
        self.favorite_button = None
        self.log_as_button = None
        try: 
            self.favorite_button = self.driver.find_element_by_xpath('//input[@value="AddRelation"]')
        except NoSuchElementException: 
            pass
        try:
             self.log_as_button = self.driver.find_element_by_link_text("Log as member")
        except NoSuchElementException:  
            pass
        
    def click_on_add_friend(self):
        if self.favorite_button is not None : 
            self.favorite_button.click()
        return self
    
    def click_on_log_as_member(self):
        if self.log_as_button is not None :
            self.log_as_button.click()
        return self
        
        