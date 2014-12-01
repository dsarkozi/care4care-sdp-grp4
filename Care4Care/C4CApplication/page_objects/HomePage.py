from C4CApplication.page_objects.FixedPage import FixedPage
from C4CApplication.page_objects.MyCare4Care import MyCare4Care
from selenium.webdriver.common.by import By


import time


class HomePage(FixedPage):
        
    def login_successful(self, mail, password):
        #Checker l'url
        #self.driver.get('%s%s' % (self.live_server_url, ''))
        
        #On fait le test
        time.sleep(1)
        mail_input = self.driver.find_element(By.NAME, 'email')
        mail_input.send_keys(mail)
        
        time.sleep(1)
        password_input = self.driver.find_element(By.NAME, 'password')
        password_input.send_keys(password)
        
        time.sleep(1)
        login_button = self.driver.find_element(By.XPATH, '//input[@value="Login"]')
        login_button.click()
        
        return MyCare4Care(self.driver)
    
    def quick_login_successful(self, mail, password):
        mail_input = self.driver.find_element(By.NAME, 'email')
        mail_input.send_keys(mail)
        password_input = self.driver.find_element(By.NAME, 'password')
        password_input.send_keys(password)
        login_button = self.driver.find_element(By.XPATH, '//input[@value="Login"]')
        login_button.click()
        return MyCare4Care(self.driver)

    def click_on_job(id):
        pass