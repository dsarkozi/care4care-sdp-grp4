from C4CApplication.simulator.super_class import MySeleniumTests
from C4CApplication.page_objects.HomePage import HomePage
from selenium import webdriver


import time


class UserAccountTest(MySeleniumTests):
    
    def login_test(self):
        self.populate_db()
        
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        
        home_page = HomePage(self.selenium)
        #home_page = HomePage(webdriver.Firefox())
        home_page.login_successful('mathieu.jadin@student.uclouvain.be', 'azertyuiop')
        
        '''
        time.sleep(1)
        username_input = self.selenium.find_element_by_name("email")
        username_input.send_keys('mathieu.jadin@student.uclouvain.be')
        time.sleep(1)
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('azertyuiop')
        time.sleep(1)
        self.selenium.find_element_by_xpath('//input[@value="Login"]').click()
        time.sleep(1)
        '''
        
        time.sleep(1)
        
        self.assertEqual(0, 0)
        return True
        
    def logoff_test(self):
        self.populate_db()
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        page = HomePage(self.selenium)
        page = page.quick_login_successful('olivier.bonaventure@gmail.com', 'azertyuiop')
        
        time.sleep(seconds)
        page.log_out()
        time.sleep()
        
        self.assertEqual(0, 0)
        return True
        
    
    def create_member_account_test(self):
        pass
    
    def create_non_member_account_test(self):
        pass
    
    def create_verified_member_test(self): #TODO keep this test?
        pass
    
    def delete_account_test(self):
        pass
    
    def update_to_volunteer_test(self):
        pass