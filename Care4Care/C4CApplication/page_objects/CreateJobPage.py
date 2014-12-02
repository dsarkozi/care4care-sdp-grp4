from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
#from C4CApplication.page_objects.HomePage import HomePage
from C4CApplication.page_objects.FixedPage import FixedPage

import time


class CreateJobPage(FixedPage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.title_input               = self.driver.find_element_by_name('title')
        self.desc_input                = self.driver.find_element_by_name('desc')
        self.branch_radio_button       = self.driver.find_element_by_name('branches')
        self.categories_radio_button   = self.driver.find_element_by_name('categories')
        self.frequency_radio_button    = self.driver.find_element_by_name('frequency')
        self.month_select              = Select(self.driver.find_element_by_tag_name('select'))
        # TODO la date 
        self.subfrequency_radio_button = self.driver.find_element_by_name('subfrequency')
        self.visibility_radio_button   = self.driver.find_element_by_name('visibility')
        self.post_req_button           = self.driver.find_element_by_xpath('//input[@value="Post request"]')
        
    def create_job(self, title, descr, branch, cat, freq, month, subfreq, visibility): 
        self.title_input.send_keys(title)
        self.desc_input.send_keys(descr)
        self.branch_radio_button.click() # TODO  choix de la branche
        self.categories_radio_button.click() # TODO choix de la cat
        self.frequency_radio_button.click() # TODO
        if subfreq is not None :
            self.subfrequency_radio_button.click() # TODO
        if month is not None :
            self.month_select.select_by_visible_text(month)
        self.visibility_radio_button.click() # TODO
        return self
      
    def click_on_post_req(self):
        self.post_req_button.click()
        #return HomePage(driver) # TODO Quentin debug son HomePage
