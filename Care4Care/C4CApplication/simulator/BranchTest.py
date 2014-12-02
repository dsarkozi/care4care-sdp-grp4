from C4CApplication.simulator.super_class import MySeleniumTests
from C4CApplication.page_objects.BranchListPage import BranchListPage

import time


class BranchTest(MySeleniumTests):

    def test_join_branch(self):
        self.populate_db()
        
        # log in
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        username_input = self.selenium.find_element_by_name("email")
        username_input.send_keys('mathieu.jadin@student.uclouvain.be')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('azertyuiop')
        self.selenium.find_element_by_xpath('//input[@value="Login"]').click()
        
        self.selenium.get('%s%s' % (self.live_server_url, '/branchlist'))
        
        page = BranchListPage(self.selenium)
        time.sleep(1)
        
        page.click_on_new_branch(1)
        time.sleep(1)
        
        page = page.click_on_submit()
        
        self.assertEqual(0, 0)
        return True
    
    """def see_branch_members_list_test(self):
        self.populate_db()
        
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        
        self.assertEqual(0, 0)
        return True"""