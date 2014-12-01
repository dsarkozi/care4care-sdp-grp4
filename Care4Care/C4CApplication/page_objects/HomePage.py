from C4CApplication.page_objects.FixedPage import FixedPage
from C4CApplication.page_objects.MyCare4Care import MyCare4Care
from C4CApplication.page_objects.CreateJobPage import CreateJobPage
from selenium.webdriver.common.by import By


import time


class HomePage(FixedPage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.mail_input = self.driver.find_element(By.NAME, 'email')
        self.password_input = self.driver.find_element(By.NAME, 'password')
        self.login_button = self.driver.find_element(By.XPATH, '//input[@value="Login"]')
        self.sign_up_button = self.driver.find_element(By.XPATH, '//input[@value="Sign up"]')
        
    def login_successful(self, mail, password):
        time.sleep(1)
        self.mail_input.send_keys(mail)
        
        time.sleep(1)
        self.password_input.send_keys(password)
        
        time.sleep(1)
        self.login_button.click()
        
        return MyCare4Care(self.driver)
    
    def quick_login_successful(self, mail, password):
        self.mail_input.send_keys(mail)
        self.password_input.send_keys(password)
        self.login_button.click()
        return MyCare4Care(self.driver)
    
    def click_on_sign_up(self):
        self.sign_up_button.click()
        return CreateJobPage(self.driver)