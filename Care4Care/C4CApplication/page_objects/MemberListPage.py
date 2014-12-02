from C4CApplication.page_objects.FixedPage import FixedPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


import time


class MemberListPage(FixedPage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.buttons_promote_verified   = self.driver.find_elements_by_xpath('//a[@value="promote_verified"]')
        self.buttons_no_more_verified   = self.driver.find_elements_by_xpath('//a[@value="no_more_verified"]')
        self.buttons_promote_volunteer  = self.driver.find_elements_by_xpath('//a[@value="promote_volunteer"]')
        self.buttons_no_more_volunteer  = self.driver.find_elements_by_xpath('//a[@value="no_more_volunteer"]')
        self.buttons_remove_from_branch = self.driver.find_elements_by_xpath('//a[@value="remove_from_branch"]')
        
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
        print("self.buttons_promote_volunteer = "+str(self.buttons_promote_volunteer))
        self.buttons_promote_volunteer[num].click()
        time.sleep(1)
        Alert(self.driver).accept()
        return self