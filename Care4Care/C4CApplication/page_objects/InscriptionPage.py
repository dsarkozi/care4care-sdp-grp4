from C4CApplication.page_objects.FixedPage import FixedPage
from C4CApplication.page_objects.MyCare4Care import MyCare4Care
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


import time


class InscriptionPage(FixedPage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.email            = self.driver.find_element(By.NAME, 'mail')
        self.password         = self.driver.find_element(By.NAME, 'password')
        self.confirm          = self.driver.find_element(By.NAME, 'confirm')
        self.first_name_input = self.driver.find_element(By.NAME, 'first_name')
        self.last_name_input  = self.driver.find_element(By.NAME, 'last_name')
        self.genders          = self.driver.find_elements(By.NAME, 'gender')
        
        self.street           = self.driver.find_element(By.NAME, 'street')
        self.zip              = self.driver.find_element(By.NAME, 'zip')
        self.town             = self.driver.find_element(By.NAME, 'town')
        
        self.fixe_phone       = self.driver.find_element(By.NAME, 'telephone')
        self.mobile_phone     = self.driver.find_element(By.NAME, 'mobile')
        
        self.birth_day = Select(self.driver.find_element(By.NAME, 'birthday_day'))
        self.birth_month = Select(self.driver.find_element(By.NAME, 'birthday_month'))
        self.birth_year = Select(self.driver.find_element(By.NAME, 'birthday_year'))
        
        self.branches = self.driver.find_elements(By.NAME, 'branch')
        self.tags = self.driver.find_elements(By.NAME, 'tag')
        
        self.submit = self.donate_button = self.driver.find_element_by_xpath('//input[@value="Register"]')
        
    def set_global_field(self, first_name, last_name, email, password, gender, b_day, \
                         b_month, b_year, street, zip, town, fix, mobile, list_branch, tag_num):
        
        self.first_name_input.send_keys(first_name)
        time.sleep(1)
        
        self.last_name_input.send_keys(last_name)
        time.sleep(1)
        
        self.email.send_keys(email)
        time.sleep(1)
        
        self.password.send_keys(password)
        time.sleep(1)
        self.confirm.send_keys(password)
        time.sleep(1)
        
        self.confirm.send_keys(password)
        time.sleep(1)
        
        if gender == 'M' : 
            self.genders[0].click()
        else: 
            self.genders[1].click()
        time.sleep(1)
        
        self.street.send_keys(street)
        time.sleep(1)
        
        self.zip.send_keys(zip)
        time.sleep(1)
        
        self.town.send_keys(town)
        time.sleep(1)
        
        self.birth_day.select_by_visible_text(b_day)
        time.sleep(1)
        self.birth_month.select_by_visible_text(b_month)
        time.sleep(1)
        self.birth_year.select_by_visible_text(b_year)
        time.sleep(1)
        
        self.fixe_phone.send_keys(fix)
        self.mobile_phone.send_keys(mobile)
        time.sleep(1)
        
        for branch in list_branch: 
            self.branches[branch].click()
            time.sleep(1) 
        
        if tag_num >= 0 and tag_num < 2 : 
            self.tags[tag_num].click()
            time.sleep(1)
        
        return self
        
    def click_on_submit(self):
        self.submit.click()
        return self
        
    # useless
    """def create_member(self, first_name, last_name, email, password, birthdate, \
                      street, number, zip, town, branch, fixe_phone='', mobile_phone=''):
        
        self.set_global_field(first_name, last_name, email, password, birthdate, \
                              street, number, zip, town, fixe_phone, mobile_phone)
        
        self.branch.select_by_visible_text(branch)
        time.sleep(1)
        
        self.member_type[1].click()
        time.sleep(1)
        
        self.submit.click()
        
        return self
    
    def create_non_member(self, first_name, last_name, email, password, birthdate, \
                      street, number, zip, town, branch, fixe_phone='', mobile_phone=''):
        
        self.set_global_field(first_name, last_name, email, password, birthdate, \
                              street, number, zip, town, fixe_phone, mobile_phone)
        
        self.branch.select_by_visible_text(branch)
        time.sleep(1)
        
        self.member_type[0].click()
        time.sleep(1)
        
        self.submit.click()
        
        return self"""
