from C4CApplication.page_objects.FixedPage import FixedPage
from selenium.webdriver.common.by import By


import time


class JobDetailsPage(FixedPage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.participate_button    = self.driver.find_element_by_xpath('//a[@value="Participate"]')
        try : 
            self.delete_job_button = self.driver.find_element_by_xpath('//a[@value="Delete job"]')
        except : 
            print("No button delete job found !")
            self.delete_job_button = None
        self.choose_member_button = self.driver.find_element_by_xpath('//a[@value="ChoiceMember"]')

    def click_on_participate(self):
        self.participate_button.click()
        return self