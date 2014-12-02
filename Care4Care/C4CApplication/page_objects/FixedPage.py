from C4CApplication.page_objects.Page import Page
#from C4CApplication.page_objects.HomePage import HomePage
#from C4CApplication.page_objects.BranchListPage import BranchListPage
from selenium.webdriver.common.by import By

import time


class FixedPage(Page):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.home        = self.driver.find_element(By.XPATH, '//a[@value="home"]')
        self.branch_list = self.driver.find_element(By.XPATH, '//a[@value="branch_list"]')
    
    def click_home(self):
        self.home.click()
        return self
    
    def click_on_care4care_branches(self):
        self.branch_list.click()
        return self
    
    def Statistics(self):
        pass
    
    def Map(self):
        pass
    
    def Start_a_branch(self):
        pass
    
    def News(self):
        pass
    
    def Jobs_at_Care4Care(self):
        pass