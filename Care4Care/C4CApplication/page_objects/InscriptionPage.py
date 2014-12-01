from C4CApplication.page_objects.FixedPage import FixedPage
from selenium.webdriver.common.by import By


import time


class InscriptionPage(FixedPage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.prenom_input = self.driver.find_element(By.NAME, 'prenom')
        self.nom_input = self.driver.find_element(By.NAME, 'nom')
        
    def create_member(self):
        pass