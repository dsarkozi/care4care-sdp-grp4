from C4CApplication.simulator.super_class import MySeleniumTests
from C4CApplication.page_objects.ModifProfilePage import ModifProfilePage


import time


class ProfileTest(MySeleniumTests):

    # database test
    """def see_data_test(self):
        self.populate_db()
        
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        
        self.assertEqual(0, 0)
        return True"""
    
    def test_update_data(self):
        self.populate_db()
        
        # log in
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        username_input = self.selenium.find_element_by_name("email")
        username_input.send_keys('mathieu.jadin@student.uclouvain.be')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('azertyuiop')
        self.selenium.find_element_by_xpath('//input[@value="Login"]').click()
        
        self.selenium.get('%s%s' % (self.live_server_url, '/modifprofile/'))
        
        page = ModifProfilePage(self.selenium)
        page = page.fill_in_info("15", "Rue bidon", "9999", "Bouseville", "010010010", "0456880045")
        time.sleep(1)
        
        page = page.click_on_submit()
        time.sleep(1)
        
        self.assertEqual(0, 0)
        return True
    
    def test_delete_picture(self):
        self.populate_db()
        
        # log in
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        username_input = self.selenium.find_element_by_name("email")
        username_input.send_keys('mathieu.jadin@student.uclouvain.be')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('azertyuiop')
        self.selenium.find_element_by_xpath('//input[@value="Login"]').click()
        
        self.selenium.get('%s%s' % (self.live_server_url, '/modifprofile/'))
        time.sleep(1)
        
        page = ModifProfilePage(self.selenium)
        page = page.click_on_delete_picture()
        time.sleep(1)
        
        self.assertEqual(0, 0)
        return True
    
    def test_delete_account(self):
        self.populate_db()
        
        # log in
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        username_input = self.selenium.find_element_by_name("email")
        username_input.send_keys('mathieu.jadin@student.uclouvain.be')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('azertyuiop')
        self.selenium.find_element_by_xpath('//input[@value="Login"]').click()
        
        self.selenium.get('%s%s' % (self.live_server_url, '/modifprofile/'))
        time.sleep(1)
        
        page = ModifProfilePage(self.selenium)
        page = page.click_on_delete_account()
        time.sleep(1)
        
        self.assertEqual(0, 0)
        return True
    
    # TODO c'est du details, on dera ca dans les simulations (dixit mathieu)
    """def confidentiality_test(self):
        self.populate_db()
        
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        
        self.assertEqual(0, 0)
        return True"""