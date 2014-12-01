from C4CApplication.page_objects.Page import Page
from C4CApplication.page_objects.HomePage import HomePage


class MyCare4Care(Page):
    
    def __init__(self, driver):
        super().__init__(driver)
        
    def log_out(self):
        logout_button = self.driver.find_element(By.XPATH, '//input[@value="Logout"]')
        logout_button.click()
        return HomePage(self.driver)