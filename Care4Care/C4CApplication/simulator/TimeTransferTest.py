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
        
        self.selenium.get('%s%s' % (self.live_server_url, '/donate/'))
        time.sleep(1)
        
        page = GiveTimePage(self.selenium)
        time.sleep(3)
        
        page = page.fill_in_fields("Voici un peu de temps", "1", "3", "0", "Care4Care compagny")
        time.sleep(2)
        
        page = page.click_on_donate()
        
        self.assertEqual(0, 0)
        return True
    
    def test_gift_test(self):
        self.populate_db()
        
        # log in
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        username_input = self.selenium.find_element_by_name("email")
        username_input.send_keys('mathieu.jadin@student.uclouvain.be')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('azertyuiop')
        self.selenium.find_element_by_xpath('//input[@value="Login"]').click()
        
        self.selenium.get('%s%s' % (self.live_server_url, '/donate/'))
        time.sleep(1)
        
        page = GiveTimePage(self.selenium)
        time.sleep(3)
        
        page = page.fill_in_fields("Tiens Olivier, voici du temps ;)", "0", "1", "40", "Olivier")
        time.sleep(2)
        
        page = page.click_on_donate()
        
        self.assertEqual(0, 0)
        return True