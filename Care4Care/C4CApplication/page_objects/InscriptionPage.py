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
        
        #self.member_type = self.driver.find_element(By.NAME, 'member_type')
        self.member_type = self.driver.find_element(By.XPATH, "//input[@name='member_type']")
        #self.member_type = self.driver.find_element(By.ID, value="member_type_form")
        
        self.branch = self.driver.find_element(By.NAME, 'branch')
        self.fixe_phone = self.driver.find_element(By.NAME, 'fixe_phone')
        self.mobile_phone = self.driver.find_element(By.NAME, 'mobile_phone')
        
    def create_member(self, first_name, last_name, email, password, birthdate, \
                      street, number, zip, town, member_type, branch, fixe_phone='', mobile_phone=''):
        '''
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
        '''
        print("self.member_type = "+str(self.member_type))
        self.member_type.click()
        time.sleep(2)
        
        return self