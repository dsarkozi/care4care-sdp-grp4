from C4CApplication.simulator.super_class import MySeleniumTests


import time


class TimeTransferTest(MySeleniumTests):
    
    def donation_test(self):
        self.populate_db()
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        page = HomePage(self.selenium)
        page = page.quick_login_successful('olivier.bonaventure@gmail.com', 'azertyuiop')
        
        page = page.click_on_give_time()
        
        
        self.assertEqual(0, 0)
        return True
    
    def gift_test(self):
        self.populate_db()
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        page = HomePage(self.selenium)
        page = page.quick_login_successful('olivier.bonaventure@gmail.com', 'azertyuiop')
        
        self.assertEqual(0, 0)
        return True