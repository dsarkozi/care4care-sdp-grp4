from C4CApplication.page_objects.Page import Page
from selenium.webdriver.common.by import By


class FixedPage(Page):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.home        = self.driver.find_element(By.XPATH, '//a[@id="home"]')
        self.branch_list = self.driver.find_element(By.XPATH, '//a[@id="branch_list"]')
    
    def click_home(self):
        self.home.click()
        return self
    
    def click_on_care4care_branches(self):
        self.branch_list.click()
        return self
    
    def Jobs_at_Care4Care(self):
        pass