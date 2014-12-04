from C4CApplication.page_objects.FixedPage import FixedPage
from selenium.webdriver.common.by import By


class ProfilePage(FixedPage):
    
    def __init__(self, driver):
        super().__init__(driver)
        modif_profile_button = self.driver.find_element_by_xpath('//a[@id="modif_profile"]')
    
    def click_on_modif_profile(self):
        self.modif_profile_button.click()
        return self