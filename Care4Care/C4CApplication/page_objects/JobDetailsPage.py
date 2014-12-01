from C4CApplication.page_objects.FixedPage import FixedPage
from selenium.webdriver.common.by import By


import time


class JobDetailsPage(FixedPage):
    
    def __init__(self, driver):
        super().__init__(driver)
        #self.participate_button   = self.driver.find_element_by_name('Participate')
        #self.delete_job_button    = self.driver.find_element_by_name('Delete job')
        #self.choose_member_button = self.driver.find_element_by_name('ChoiceMember')
        # ca faire du boudin