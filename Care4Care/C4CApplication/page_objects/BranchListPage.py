import time

from C4CApplication.page_objects.FixedPage import FixedPage
from C4CApplication.page_objects.MemberListPage import MemberListPage


class BranchListPage(FixedPage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.check_box = self.driver.find_elements_by_name('branch_list')
        self.links_branch_details = self.driver.find_elements_by_xpath("//a[@class='branch_details']")
        self.submit_button = self.driver.find_element_by_xpath('//input[@id="submit_button"]')
        
    def click_on_new_branch(self, num):
        self.check_box[num].click()
        return self
    
    def click_on_branch_details(self, num): 
        self.links_branch_details[num].click()
        time.sleep(1)
        return MemberListPage(self.driver)
        
    def click_on_submit(self):
        self.submit_button.click()
        return self
