from C4CApplication.page_objects.FixedPage import FixedPage
from C4CApplication.page_objects.MyCare4Care import MyCare4Care
from C4CApplication.page_objects.CreateJobPage import CreateJobPage
from C4CApplication.page_objects.InscriptionPage import InscriptionPage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


import time


class HomePage(FixedPage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.mail_input     = None
        self.password_input = None
        self.login_button   = None
        self.sign_up_button = None
        self.logout_button  = None
        try: 
            self.mail_input     = self.driver.find_element(By.NAME, 'email')
            self.password_input = self.driver.find_element(By.NAME, 'password')
            self.login_button   = self.driver.find_element(By.XPATH, '//input[@id="Login"]')
            self.sign_up_button = self.driver.find_element(By.XPATH, '//input[@id="sing_up"]') # TODO up
        except NoSuchElementException:  # this is a normal behaviour : that's not the same buttons 
            pass # there depending on if you're log or not
        try: 
            self.logout_button  = self.driver.find_element(By.XPATH, '//a[@id="Logout"]') 
        except NoSuchElementException:  # normal 
            pass 
        
        self.want_to_help_button = self.driver.find_elements(By.CLASS_NAME, "myButton")[0]
        self.need_help_button = self.driver.find_elements(By.CLASS_NAME, "myButton")[1]
        # TODO recup les job offers et job demands
        self.job_offers_links = self.driver.find_elements(By.CLASS_NAME, "job_offer")
        self.job_demands_links = self.driver.find_elements(By.CLASS_NAME, "job_demand")
        
    def login_successful(self, mail, password):
        time.sleep(1)
        self.mail_input.send_keys(mail)
        
        time.sleep(1)
        self.password_input.send_keys(password)
        
        time.sleep(1)
        self.login_button.click()
        
        return MyCare4Care(self.driver) 
    
    def login_fail(self, mail, password):
        time.sleep(1)
        self.mail_input.send_keys(mail)
        
        time.sleep(1)
        self.password_input.send_keys(password)
        
        time.sleep(1)
        self.login_button.click()
        
        return self
    
    def quick_login_successful(self, mail, password):
        self.mail_input.send_keys(mail)
        self.password_input.send_keys(password)
        self.login_button.click()
        return MyCare4Care(self.driver)
    
    def click_on_sign_up(self):
        self.sign_up_button.click()
        return InscriptionPage(self.driver)
    
    def click_on_logout(self):
        if self.logout_button is not None: 
            self.logout_button.click()
        time.sleep(1)
        return HomePage(self.driver)
    
    def click_on_i_want_to_help(self):
        self.want_to_help_button.click()
        time.sleep(1)
        return CreateJobPage(self.driver)
    
    def click_on_i_need_help(self):
        self.need_help_button.click()
        time.sleep(1)
        return CreateJobPage(self.driver)
    
    def click_on_last_offer(self):
        self.job_offers_links[len(self.job_offers_links)-1].click()
        return self
