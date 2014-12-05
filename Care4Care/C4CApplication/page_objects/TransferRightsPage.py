from C4CApplication.page_objects.FixedPage import FixedPage
from selenium.webdriver.common.by import By

import time


class TransferRightsPage(FixedPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.mail_bpa_input = self.driver.find_element_by_name('email_new_BPAdmin')
        self.change_bpa_button = self.driver.find_element_by_xpath('//input[@class="btn"]')
        
    def set_email_new_bpa(self, email):
        self.mail_bpa_input.send_keys(email)
        return self
    
    def click_on_change(self):
        self.change_bpa_button.click()
        return self
        