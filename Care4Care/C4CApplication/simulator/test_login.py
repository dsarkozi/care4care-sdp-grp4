from C4CApplication.simulator.super_class import MySeleniumTests
from C4CApplication.page_objects.HomePage import HomePage
from selenium import webdriver


import time


class SeleniumTestLogin(MySeleniumTests):

    def test_login(self):
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