from C4CApplication.simulator.super_class import MySeleniumTests


import time


class BranchOfficerTest(MySeleniumTests):

    def remove_branch_member_test(self):
        self.populate_db()
        
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        
        self.assertEqual(0, 0)
        return True
    
    def log_as_other_member_test(self):
        self.populate_db()
        
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        
        self.assertEqual(0, 0)
        return True