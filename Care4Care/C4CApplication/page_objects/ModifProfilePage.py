from C4CApplication.page_objects.FixedPage import FixedPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

import time


class ModifProfilePage(FixedPage):
    
    def __init__(self, driver):
        super().__init__(driver)
        buttons = self.driver.find_elements_by_xpath('//a[@class="btn"]') # all elements of the class "btn"
        
        self.browse_button = self.driver.find_element_by_name('picture')
        self.delete_pic_button = buttons[len(buttons)-2]
        self.street_input       = self.driver.find_element_by_name('street')
        self.postal_code_input  = self.driver.find_element_by_name('zip')
        self.town_input         = self.driver.find_element_by_name('town')
        self.phone_num_input    = self.driver.find_element_by_name('fixed_phone')
        self.mobile_phone_input = self.driver.find_element_by_name('mobile_phone')
        self.submit_button = self.driver.find_element_by_xpath('//input[@value="Submit"]')
        self.delete_account_button = self.driver.find_element_by_xpath("//a[@id='delete_account']")
        
    def fill_in_info(self, street, zip, town, phone, mobile, clear=True):
        if clear : 
            self.street_input.clear()
            self.postal_code_input.clear()
            self.town_input.clear()
            self.phone_num_input.clear()
            self.mobile_phone_input.clear()
            
        self.street_input.send_keys(street)
        time.sleep(1)
        self.postal_code_input.send_keys(zip)
        time.sleep(1)
        self.town_input.send_keys(town)
        time.sleep(1)
        self.phone_num_input.send_keys(phone)
        time.sleep(1)
        self.mobile_phone_input.send_keys(mobile)
        time.sleep(1)
        return self
    
    def click_on_submit(self):
        self.submit_button.click()
        return self
    
    def click_on_delete_picture(self):
        self.delete_pic_button.click()
        return self
    
    def click_on_delete_account(self):
        self.delete_account_button.click()
        time.sleep(1)
        Alert(self.driver).accept()
        time.sleep(1)
        return self