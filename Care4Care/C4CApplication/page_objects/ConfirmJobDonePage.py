from C4CApplication.page_objects.FixedPage import FixedPage
from selenium.webdriver.common.by import By

import time

# A quoi sert la fixedPage ? Il faut la mettre ici aussi ?
class ConfirmJobDonePage(FixedPage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.job_time_input = self.driver.find_element_by_name("time_to_pay")
        self.confirm_button = self.selenium.find_element_by_xpath('//input[@value="Confirm"]')
        
    def enter_time_to_pay(self, time):
        self.job_time_input.send_keys(str(time))
        return self
        
    def click_on_confirm(self):
        self.confirm_button.click()
        #return HomePage(driver)