from C4CApplication.page_objects.FixedPage import FixedPage
from selenium.webdriver.common.by import By


import time


class BranchListPage(Page):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.check_box = self.driver.find_elements_by_name('branch_list')
        self.submit_button = self.driver.find_element_by_xpath('//input[@value="Submit changes"]')
        
    def click_on_new_branch(self, num): # TODO
        self.check_box[num].click()
        return self
        
    def click_on_submit(self):
        self.submit_button.click()
        return self