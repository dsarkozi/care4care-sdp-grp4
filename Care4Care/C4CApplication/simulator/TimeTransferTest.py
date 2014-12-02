from C4CApplication.simulator.super_class import MySeleniumTests
from C4CApplication.page_objects.HomePage import HomePage
from C4CApplication.page_objects.GiveTimePage import GiveTimePage


import time


class TimeTransferTest(MySeleniumTests):
    
    def test_donation(self):
        self.populate_db()
        
        # log in
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        username_input = self.selenium.find_element_by_name("email")
        username_input.send_keys('mathieu.jadin@student.uclouvain.be')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('azertyuiop')
        self.selenium.find_element_by_xpath('//input[@value="Login"]').click()
        
        print("Let's go !")
        #page = page.click_on_give_time()
        self.selenium.get('%s%s' % (self.live_server_url, '/donate/'))
        
        time.sleep(1)
        page = GiveTimePage(self.selenium)
        
        print("OK creation of the page")
        
        
        self.assertEqual(0, 0)
        return True
    
    """def gift_test(self):
        self.populate_db()
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        page = HomePage(self.selenium)
        page = page.quick_login_successful('olivier.bonaventure@gmail.com', 'azertyuiop')
        
        self.assertEqual(0, 0)
        return True"""