from C4CApplication.page_objects.FixedPage import FixedPage
from selenium.webdriver.common.by import By


import time


class BranchListPage(FixedPage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.check_box = self.driver.find_elements_by_name('branch_list')
        self.links_branch_details = self.driver.find_elements_by_xpath("//a[@value='branch_details']")
        self.submit_button = self.driver.find_element_by_xpath('//input[@id="submit_button"]')
        
    def click_on_new_branch(self, num):
        self.check_box[num].click()
        return self
    
    def click_on_branch_details(self, num): # TODO
        self.links_branch_details[num].click()
        return self
        
    def click_on_submit(self):
        self.submit_button.click()
        return self
