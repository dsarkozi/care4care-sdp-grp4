from C4CApplication.page_objects.FixedPage import FixedPage
from C4CApplication.page_objects.MemberDetailsPage import MemberDetailsPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


import time


class MemberListPage(FixedPage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.buttons_promote_verified   = self.driver.find_elements_by_xpath('//a[@id="promote_verified"]')
        self.buttons_no_more_verified   = self.driver.find_elements_by_xpath('//a[@id="no_more_verified"]')
        self.buttons_promote_volunteer  = self.driver.find_elements_by_xpath('//a[@id="promote_volunteer"]')
        self.buttons_no_more_volunteer  = self.driver.find_elements_by_xpath('//a[@id="no_more_volunteer"]')
        self.buttons_remove_from_branch = self.driver.find_elements_by_xpath('//a[@id="remove_from_branch"]')
        self.members_links = self.driver.find_elements_by_class_name("member_details")
        
    def click_on_member(self, num):
        if len(self.members_links) >= num: 
            self.members_links[num].click()
        time.sleep(1)
        return MemberDetailsPage(self.driver)
            
    def click_on_remove_from_branch(self, num):
        self.buttons_remove_from_branch[num].click()
        time.sleep(1)
        Alert(self.driver).accept()
        return self
    
    def click_on_promote_verified(self, num):
        self.buttons_promote_verified[num].click()
        time.sleep(1)
        Alert(self.driver).accept()
        return self
    
    def click_on_promote_volunteer(self, num):
        self.buttons_promote_volunteer[num].click()
        time.sleep(1)
        Alert(self.driver).accept()
        return self