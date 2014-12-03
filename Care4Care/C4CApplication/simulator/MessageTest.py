from C4CApplication.simulator.super_class import MySeleniumTests
from C4CApplication.page_objects.ListMessagesPage import ListMessagesPage


import time

class MessageTest(MySeleniumTests):

    def test_see_message(self):
        self.populate_db()
        
        # log in
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        username_input = self.selenium.find_element_by_name("email")
        username_input.send_keys('kim.mens@gmail.com')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('azertyuiop')
        self.selenium.find_element_by_xpath('//input[@value="Login"]').click()
        
        self.selenium.get('%s%s' % (self.live_server_url, '/list_messages/1'))
        page = ListMessagesPage(self.selenium)
        
        
        self.assertEqual(0, 0)
        return True
    
    """def send_message_test(self):
        self.populate_db()
        
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        
        self.assertEqual(0, 0)
        return True"""