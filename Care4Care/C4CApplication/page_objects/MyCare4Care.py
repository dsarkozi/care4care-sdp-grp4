from C4CApplication.page_objects.FixedPage import FixedPage
#from C4CApplication.page_objects.HomePage import HomePage
from selenium.webdriver.common.by import By


class MyCare4Care(FixedPage):
    
    def give_time(self):
        #give_time_button = self.driver.find_element(By.XPATH, )
        pass
    
    def register_job_done(self):
        pass
    
    def i_need_help(self):
        pass
    
    def i_want_to_help(self):
        pass
        
    def profile(self):
        pass
    
    def messages(self):
        pass
    
    def change(self):
        pass
    
    def favorites(self):
        pass
    
    def account_and_stats(self):
        pass
    
    def log_out(self):
        logout_button = self.driver.find_element(By.XPATH, '//input[@value="Logout"]')
        logout_button.click()
        #return HomePage(self.driver)