from C4CApplication.page_objects.FixedPage import FixedPage
from selenium.webdriver.common.by import By

import time


class CreateBranchPage(FixedPage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.name_input = self.driver.find_element_by_name('name')
        self.town_input = self.driver.find_element_by_name('town')
        self.branch_off_input = self.driver.find_element_by_name('branch_off')
        self.address_input = self.driver.find_element_by_name('address')
        self.submit_button = self.submit_button = self.driver.find_element_by_xpath('//input[@value="Submit"]')
        
    def fill_in_info(self, name, town, br_of, addr): 
        self.name_input.send_keys(name)
        self.town_input.send_keys(town)
        self.branch_off_input.send_keys(br_of)
        self.address_input.send_keys(addr)
        return self
    
    def click_on_submit(self):
        self.submit_button.click()
        return self # TODO