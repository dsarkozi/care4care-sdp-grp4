from C4CApplication.unit_test.super_class import MySeleniumTests
from C4CApplication.page_objects.MemberDetailsPage import MemberDetailsPage
from C4CApplication.page_objects.MemberListPage import MemberListPage

import time


class BranchOfficerTest(MySeleniumTests):

    def test_remove_branch_member(self):
        self.populate_db()
        
        # log in
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        page = HomePage(self.selenium)
        page = page.quick_login_successful('kim.mens@gmail.com', 'azertyuiop')
        
        self.selenium.get('%s%s' % (self.live_server_url, '/branchdetails/LLN/'))
        time.sleep(1)
        
        page = MemberListPage(self.selenium)
        time.sleep(1)
        
        page = page.click_on_remove_from_branch(1)
        time.sleep(1)
        
        self.assertEqual(0, 0)
        return True
    
    def test_log_as_other_member(self):
        self.populate_db()
        
        # log in
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        page = HomePage(self.selenium)
        page = page.quick_login_successful('kim.mens@gmail.com', 'azertyuiop')
        
        self.selenium.get('%s%s' % (self.live_server_url, '/memberdetails/olivier.mauvaventure%40gmail.com'))
        time.sleep(1)

        page = MemberDetailsPage(self.selenium)
        time.sleep(1)
        
        page = page.click_on_log_as_member()
        time.sleep(1)
        
        self.assertEqual(0, 0)
        return True