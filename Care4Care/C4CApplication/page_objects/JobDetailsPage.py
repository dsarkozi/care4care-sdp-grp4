from C4CApplication.page_objects.FixedPage import FixedPage
from selenium.webdriver.common.by import By


import time


class JobDetailsPage(FixedPage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.choose_member_buttons = None
        self.delete_job_button     = None
        self.participate_button    = None
        try : self.delete_job_button = self.driver.find_elements_by_xpath('//a[@value="Delete job"]')
        except : pass
        try : self.choose_member_buttons = self.driver.find_elements_by_xpath("//a[@value='choose_this_member']")
        except : pass
        try : self.participate_button = self.driver.find_element_by_xpath('//a[@value="Participate"]')
        except : pass

    def click_on_participate(self):
        self.participate_button.click()
        return self
    
    def click_on_choose_member(self):
        self.choose_member_buttons[0].click()
        return self