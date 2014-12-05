from C4CApplication.page_objects.FixedPage import FixedPage
from selenium.webdriver.common.by import By

import time


class CreateBranchPage(FixedPage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.name_input = self.driver.find_element_by_name('name')
        self.branch_town_input = self.driver.find_element_by_name('branch_town')
        self.branch_off_input = self.driver.find_element_by_name('branch_off')
        self.street_input = self.driver.find_element_by_name('street')
        self.zip_input = self.driver.find_element_by_name('zip')
        self.town_input = self.driver.find_element_by_name('town')
        self.submit_button = self.submit_button = self.driver.find_element_by_xpath('//input[@id="Submit"]')
        
    def fill_in_info(self, name, br_town, br_of, street, zip, town): 
        self.name_input.send_keys(name)
        self.branch_town_input.send_keys(br_town)
        self.branch_off_input.send_keys(br_of)
        self.street_input.send_keys(street)
        self.zip_input.send_keys(zip)
        self.town_input.send_keys(town)
        return self
    
    def click_on_submit(self):
        self.submit_button.click()
        return self # TODO