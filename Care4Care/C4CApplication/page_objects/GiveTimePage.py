from C4CApplication.page_objects.Page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert

import time


#For DonateTime.html
class GiveTimePage(Page):
    
    def __init__(self, driver):
        super().__init__(driver) 
        self.message_input = self.driver.find_element_by_name('message')
        self.days_input = self.driver.find_element_by_name('days')
        self.hours_input = self.driver.find_element_by_name('hours')
        self.minutes_input = self.driver.find_element_by_name('minutes')
        self.radio_button_receipient = self.driver.find_elements_by_name('receiver')
        self.user_select = Select(self.driver.find_element_by_tag_name('select'))
        self.donate_button = self.driver.find_element_by_xpath('//input[@id="donate"]')
        
    def click_on_donate(self):
        self.donate_button.click()
        time.sleep(1)
        Alert(self.driver).accept()
        return self
    
    def fill_in_fields(self, message, days, hours, min, user):
        self.message_input.send_keys(message)
        time.sleep(1)
        self.days_input.send_keys(days)
        time.sleep(1)
        self.hours_input.send_keys(hours)
        time.sleep(1)
        self.minutes_input.send_keys(min)
        time.sleep(1)
        if user == "Care4Care compagny" : 
            self.radio_button_receipient[0].click()
        else: 
            self.radio_button_receipient[1].click()
            self.user_select.select_by_visible_text(user)
        return self
    