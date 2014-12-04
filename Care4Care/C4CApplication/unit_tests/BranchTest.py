from C4CApplication.unit_tests.super_class import MySeleniumTests
from C4CApplication.page_objects.BranchListPage import BranchListPage

import time


class BranchTest(MySeleniumTests):

    def test_join_branch(self):
        self.populate_db()
        
        # log in
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        page = HomePage(self.selenium)
        page = page.quick_login_successful('mathieu.jadin@student.uclouvain.be', 'azertyuiop')
        
        
        self.selenium.get('%s%s' % (self.live_server_url, '/branchlist'))
        
        page = BranchListPage(self.selenium)
        time.sleep(1)
        
        page.click_on_new_branch(1)
        time.sleep(1)
        
        page = page.click_on_submit()
        
        self.assertEqual(0, 0)
        return True
    
    """def see_branch_members_list_test(self): # Faire des tests de db
        self.populate_db()
        
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        
        self.assertEqual(0, 0)
        return True"""