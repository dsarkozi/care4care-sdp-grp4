from C4CApplication.simulator.super_class import MySeleniumTests
from C4CApplication.page_objects.MemberDetailsPage import MemberDetailsPage

import time


class BranchOfficerTest(MySeleniumTests):

    """def test_remove_branch_member(self):
        self.populate_db()
        
        # log in
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        username_input = self.selenium.find_element_by_name("email")
        username_input.send_keys('kim.mens@gmail.com')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('azertyuiop')
        self.selenium.find_element_by_xpath('//input[@value="Login"]').click()
        
        self.selenium.get('%s%s' % (self.live_server_url, '/branchdetails/LLN/'))
        time.sleep(5)
        
        #page = MemberListPage(self.selenium)
        
        #page = page.click_on_remove_member()
        
        self.assertEqual(0, 0)
        return True"""
    
    def test_log_as_other_member(self):
        self.populate_db()
        
        # log in
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        username_input = self.selenium.find_element_by_name("email")
        username_input.send_keys('kim.mens@gmail.com')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('azertyuiop')
        self.selenium.find_element_by_xpath('//input[@value="Login"]').click()
        
        self.selenium.get('%s%s' % (self.live_server_url, '/memberdetails/olivier.mauvaventure%40gmail.com'))
        time.sleep(1)

        page = MemberDetailsPage(self.selenium)
        print("Page created")
        
        time.sleep(1)
        page = page.click_on_log_as_member()
        time.sleep(15)
        
        self.assertEqual(0, 0)
        return True