from C4CApplication.page_objects.FixedPage import FixedPage
from selenium.webdriver.common.by import By

from selenium.webdriver.common.alert import Alert


class DeleteMemberBPAPage(FixedPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.mail_input = None
        self.submit_button = None
        try: self.mail_input = self.driver.find_element(By.NAME, 'email')
        except: pass
        try: self.submit_button = self.driver.find_element(By.XPATH, '//input[@class="btn"]')
        except: pass  # this is a normal behaviour : that's not the same buttons

    def delete_member(self, member_email):
        self.mail_input.send_keys(member_email)
        self.submit_button.click()
        Alert(self.driver).accept()
