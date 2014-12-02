from C4CApplication.page_objects.FixedPage import FixedPage
from selenium.webdriver.common.by import By


import time


class JobDetailsPage(FixedPage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.participate_button    = self.driver.find_element_by_xpath('//a[@value="Participate"]')
        try : 
            self.delete_job_button = self.driver.find_elements_by_xpath('//a[@value="Delete job"]')
        except : 
            print("No button delete job found !")
            self.delete_job_button = None
        # Impossiiiiiiiiiiiible ! That fucking bullshit de merde !!!!!
        self.choose_member_buttons = self.driver.find_elements(By.PARTIAL_LINK_TEXT, 'Choose')

    def click_on_participate(self):
        self.participate_button.click()
        return self
    
    # Impossiiiiiiiiiiiible ! On ne sait pas retrouver choose_member_button
    def click_on_choose_member(self):
        print(self.choose_member_buttons)
        for m_web_el in self.choose_member_buttons:
            print(m_web_el.text)
        #self.choose_member_button.click()
        return self