from C4CApplication.page_objects.Page import FixedPage
from C4CApplication.page_objects.HomePage import HomePage


class MyCare4Care(FixedPage):
    
    def give_time(self):
        #give_time_button = self.driver.find_element(By.XPATH, )
        pass
    
    def register_job_done(self):
        pass
    
    def I_need_help(self):
        pass
    
    def I_want_to_help(self):
        pass
        
    def log_out(self):
        logout_button = self.driver.find_element(By.XPATH, '//input[@value="Logout"]')
        logout_button.click()
        return HomePage(self.driver)