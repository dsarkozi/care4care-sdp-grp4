from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
#from C4CApplication.page_objects.HomePage import HomePage
from C4CApplication.page_objects.FixedPage import FixedPage

import time


class CreateJobPage(FixedPage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.title_input               = self.driver.find_element_by_name('title')
        self.desc_input                = self.driver.find_element_by_name('description')
        self.location_input            = self.driver.find_element_by_name('place')
        self.branch_radio_buttons      = self.driver.find_elements_by_name('branches')
        
        self.start_time_input          = self.driver.find_element_by_id('id_start_time')
        self.duration_input            = self.driver.find_element_by_id('id_duration')
        self.distance_input            = self.driver.find_element_by_id('id_km')
        
        self.categories_radio_buttons  = self.driver.find_elements_by_name('category')
        self.frequency_radio_buttons   = self.driver.find_elements_by_name('frequency') # [ once, weekly, monthly ]
        
        # Once :
        self.day_select              = Select(self.driver.find_element_by_id('time_specific_day'))
        self.month_select            = Select(self.driver.find_element_by_id('time_specific_month'))
        self.year_select             = Select(self.driver.find_element_by_id('time_specific_year'))
        
        # Weekly :
        self.weekdays_check_box      = self.driver.find_elements_by_name('weekdays')
        
        # Monthly :
        self.monthdays_check_box      = self.driver.find_elements_by_name('dayrange')

        self.visibility_checkbox   = self.driver.find_elements_by_name('visibility')
        
        self.post_req_button           = self.driver.find_element_by_xpath('//input[@value="Post"]')
        
    def create_job(self, title, descr, location, branch_num, start, duration, dist, \
                   cat_num, freq_num, day, month, year, w_days, m_days, vis_list): 
        self.title_input.send_keys(title)
        self.desc_input.send_keys(descr)
        self.location_input.send_keys(location)
        self.branch_radio_buttons[branch_num].click() 
        
        self.start_time_input.clear()
        self.start_time_input.send_keys(start)
        self.duration_input.clear()
        self.duration_input.send_keys(duration)
        self.distance_input.clear()
        self.distance_input.send_keys(dist)
        
        self.categories_radio_buttons[cat_num].click()
        self.frequency_radio_buttons[freq_num].click() 
        
        if freq_num == 0:
            self.day_select.select_by_visible_text(day)
            self.month_select.select_by_visible_text(month)
            self.year_select.select_by_visible_text(year)
        elif freq_num == 1:
            for day in w_days : 
                self.weekdays_check_box[day].click()
        elif freq_num == 2:
            for day in m_days : 
                self.monthdays_check_box[day].click()  
        
        for visible in vis_list : 
            self.visibility_checkbox[visible].click()
        return self
      
    def click_on_post_req(self):
        self.post_req_button.click()
        return self 
