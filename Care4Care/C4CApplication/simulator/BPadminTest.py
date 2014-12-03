from C4CApplication.simulator.BranchOfficerTest import BranchOfficerTest
from C4CApplication.page_objects.HomePage import HomePage


import time


class BranchOfficerTest(BranchOfficerTest):

    def create_branch_test(self):
        self.populate_db()
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        page = HomePage(self.selenium)
        page = page.quick_login_successful('mathieu.jadin@student.uclouvain.be', 'azertyuiop')
        time.sleep(1)
        
        page = page.BP_click_on_new_branch()
        time.sleep(1)
        
        #TODO
        
        self.assertEqual(0, 0)
        return True
    
    def handle_volunteers_request_test(self):
        self.populate_db()
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        page = HomePage(self.selenium)
        page = page.quick_login_successful('mathieu.jadin@student.uclouvain.be', 'azertyuiop')
        time.sleep(1)
        
        #TODO
        
        self.assertEqual(0, 0)
        return True
    
    def handle_verified_member_request_test(self):
        self.populate_db()
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        page = HomePage(self.selenium)
        page = page.quick_login_successful('mathieu.jadin@student.uclouvain.be', 'azertyuiop')
        time.sleep(1)
        
        #TODO
        
        self.assertEqual(0, 0)
        return True
    
    def choose_branch_officer_test(self):
        self.populate_db()
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        page = HomePage(self.selenium)
        page = page.quick_login_successful('mathieu.jadin@student.uclouvain.be', 'azertyuiop')
        time.sleep(1)
        
        #TODO
        
        self.assertEqual(0, 0)
        return True
    
    def change_branch_officer_test(self):
        self.populate_db()
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        page = HomePage(self.selenium)
        page = page.quick_login_successful('mathieu.jadin@student.uclouvain.be', 'azertyuiop')
        time.sleep(1)
        
        #TODO
        
        self.assertEqual(0, 0)
        return True
    
    def resing_from_bp_admin_test(self):
        self.populate_db()
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        page = HomePage(self.selenium)
        page = page.quick_login_successful('mathieu.jadin@student.uclouvain.be', 'azertyuiop')
        time.sleep(1)
        
        #TODO
        
        self.assertEqual(0, 0)
        return True