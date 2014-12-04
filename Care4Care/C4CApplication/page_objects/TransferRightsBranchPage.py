from C4CApplication.page_objects.FixedPage import FixedPage
from selenium.webdriver.common.by import By

import time


class TransferRightsBranchPage(FixedPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.mail_br_of_input = self.driver.find_element_by_name('email_new_branch_officer')
        self.change_br_of_button = self.driver.find_element_by_xpath('//input[@value="Change Branch officer"]')
        #self.cancel_button = self.driver.find_element_by_partial_link_text('Change')
        
    def set_email_new_branch_off(self, email):
        self.mail_br_of_input.send_keys(email)
        return self
    
    def click_on_change(self):
        self.change_br_of_button.click()
        return self
        