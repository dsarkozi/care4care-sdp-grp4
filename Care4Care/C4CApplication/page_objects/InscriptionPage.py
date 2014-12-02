from C4CApplication.page_objects.FixedPage import FixedPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


import time


class InscriptionPage(FixedPage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.first_name_input = self.driver.find_element(By.NAME, 'first_name')
        self.last_name_input  = self.driver.find_element(By.NAME, 'last_name')
        self.email            = self.driver.find_element(By.NAME, 'email')
        self.password         = self.driver.find_element(By.NAME, 'password')
        self.birthdate        = self.driver.find_element(By.NAME, 'birthdate')
        self.number           = self.driver.find_element(By.NAME, 'number')
        self.street           = self.driver.find_element(By.NAME, 'street')
        self.zip              = self.driver.find_element(By.NAME, 'zip')
        self.town             = self.driver.find_element(By.NAME, 'town')
        self.fixe_phone       = self.driver.find_element(By.NAME, 'fixe_phone')
        self.mobile_phone     = self.driver.find_element(By.NAME, 'mobile_phone')
        self.submit           = self.driver.find_element(By.NAME, 'envoyer')
        self.member_type      = self.driver.find_elements(By.NAME, 'member_type')
        self.branch = Select(self.driver.find_element(By.NAME, 'branch'))
        
        
        
    def set_global_field(self, first_name, last_name, email, password, birthdate, \
                         street, number, zip, town, fixe_phone, mobile_phone):
        
        self.first_name_input.send_keys(first_name)
        time.sleep(1)
        
        self.last_name_input.send_keys(last_name)
        time.sleep(1)
        
        self.email.send_keys(email)
        time.sleep(1)
        
        self.password.send_keys(password)
        time.sleep(1)
        
        self.birthdate.send_keys(birthdate)
        time.sleep(1)
        
        self.street.send_keys(street)
        time.sleep(1)
        
        self.number.send_keys(number)
        time.sleep(1)
        
        self.zip.send_keys(zip)
        time.sleep(1)
        
        self.town.send_keys(town)
        time.sleep(1)
        
        self.fixe_phone.send_keys(fixe_phone)
        self.mobile_phone.send_keys(mobile_phone)
        
    def create_member(self, first_name, last_name, email, password, birthdate, \
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
        
        return self