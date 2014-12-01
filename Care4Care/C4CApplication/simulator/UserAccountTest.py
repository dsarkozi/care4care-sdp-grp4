from C4CApplication.simulator.super_class import MySeleniumTests
from C4CApplication.page_objects.HomePage import HomePage


import time


class UserAccountTest(MySeleniumTests):
    
    def test_login(self):
        self.populate_db()
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        
        home_page = HomePage(self.selenium)
        home_page.login_successful('mathieu.jadin@student.uclouvain.be', 'azertyuiop')
        time.sleep(1)
        
        self.assertEqual(0, 0)
        return True
        
        
    def test_logoff(self):
        self.populate_db()
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        page = HomePage(self.selenium)
        page = page.quick_login_successful('olivier.bonaventure@gmail.com', 'azertyuiop')
        
        time.sleep(1)
        page.log_out()
        time.sleep(1)
        
        self.assertEqual(0, 0)
        return True
    
    def test_create_member_account(self):
        self.populate_db()
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        time.sleep(1)
        
        page = HomePage(self.selenium)
        page = page.click_on_sign_up()
        time.sleep(1)
        
        page = page.create_member('Mister', 'Nobody', 'mister_nobody@gmail.com', 'azertyuiop', '1920-06-14',\
                                  'Vie', 3, 6458, 'Multilife', 'member', 'LLN')
        time.sleep(1)
        
        self.assertEqual(0, 0)
        return True
    
    def test_create_non_member_account(self):
        pass
    
    def test_create_verified_member(self): #TODO keep this test?
        pass
    
    def test_delete_account(self):
        pass
    
    def test_update_to_volunteer(self):
        pass