import time

from C4CApplication.page_objects.FixedPage import FixedPage
from selenium.webdriver.common.alert import Alert


class NewMessagePage(FixedPage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.dest_input = self.driver.find_element_by_name('receveur')
        self.subject_input = self.driver.find_element_by_name('sujet')
        self.content_input = self.driver.find_element_by_name('message')
        self.submit_button = self.driver.find_element_by_xpath('//input[@id="send_message"]')
        
    def fill_in_info(self, dest, subject, content):
        self.dest_input.send_keys(dest)
        time.sleep(1)
        self.subject_input.send_keys(subject)
        time.sleep(1)
        self.content_input.send_keys(content)
        return self
    
    def click_on_submit(self):
        self.submit_button.click()
        time.sleep(1)
        Alert(self.driver).accept()
        return self