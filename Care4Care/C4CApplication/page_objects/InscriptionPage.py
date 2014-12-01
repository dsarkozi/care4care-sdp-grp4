from C4CApplication.page_objects.FixedPage import FixedPage
from selenium.webdriver.common.by import By


import time


class InscriptionPage(FixedPage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.prenom_input = self.driver.find_element(By.NAME, 'first_name')
        self.nom_input = self.driver.find_element(By.NAME, 'last_name')
        self.email = self.driver.find_element(By.NAME, 'email')
        self.password = self.driver.find_element(By.NAME, 'password')
        self.birthdate = self.driver.find_element(By.NAME, 'birthdate')
        self.number = self.driver.find_element(By.NAME, 'number')
        self.street = self.driver.find_element(By.NAME, 'street')
        self.zip = self.driver.find_element(By.NAME, 'zip')
        self.town = self.driver.find_element(By.NAME, 'town')
        self.member_type = self.driver.find_element(By.NAME, 'member_type')
        self.branch = self.driver.find_element(By.NAME, 'branch')
        self.fixe_phone = self.driver.find_element(By.NAME, 'fixe_phone')
        self.mobile_phone = self.driver.find_element(By.NAME, 'mobile_phone')
        
    def create_member(self, first_name, last_name, email, password, birthdate, \
                      street, number, zip, town, member_type, branch, fixe_phone='', mobile_phone=''):
        return self