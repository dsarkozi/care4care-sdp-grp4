from selenium.common.exceptions import NoSuchElementException
from C4CApplication.page_objects.FixedPage import FixedPage
from selenium.webdriver.common.by import By

from selenium.webdriver.common.alert import Alert
import time


class DeleteMemberBPAPage(FixedPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.mail_input = None
        self.submit_button = None
        try:
            self.mail_input = self.driver.find_element(By.NAME, 'email')
            self.submit_button = self.driver.find_element(By.XPATH, '//input[@class="btn"]')
        except NoSuchElementException:  # this is a normal behaviour : that's not the same buttons
            pass  # there depending on if you're log or not

    def delete_member(self, member_email):
        self.mail_input.send_keys(member_email)
        self.submit_button.click()
        Alert(self.driver).accept()
