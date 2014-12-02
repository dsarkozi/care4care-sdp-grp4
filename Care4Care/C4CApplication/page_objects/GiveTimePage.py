from C4CApplication.page_objects.Page import Page
from selenium.webdriver.common.by import By

import time


class GiveTimePage(Page):
    
    def __init__(self, driver):
        super().__init__(driver) 
        self.message_input = self.driver.find_element_by_name('message')
        self.days_input = self.driver.find_element_by_name('days')
        self.hours_input = self.driver.find_element_by_name('hours')
        self.minutes_input = self.driver.find_element_by_name('minutes')
        print("message, days, hours and minutes found !")
        self.radio_button_receipient = self.driver.find_elements_by_name('receiver')
        print("receipient found : "+str(self.radio_button_receipient))
        self.user_select = Select(self.driver.find_element_by_tag_name('select'))
        print("select OK")
        self.donate_button = self.driver.find_element_by_xpath('//input[@value="Donate time"]')
        
    def click_on_donate(self):
        self.donate_button.click()
        return self
    
    def fill_in_fields(self, message, days, hours, min, user):
        self.message_input.send_keys(message)
        self.days_input.send_keys(days)
        self.hours_input.send_keys(hours)
        self.minutes_input.send_keys(min)
        if user == "Care4Care compagny" : 
            self.radio_button_receipient[0].click()
        else: 
            self.radio_button_receipient[1].click()
            self.user_select.select_by_visible_text(user)
    