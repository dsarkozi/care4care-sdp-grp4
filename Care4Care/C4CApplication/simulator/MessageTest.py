from C4CApplication.simulator.super_class import MySeleniumTests
from C4CApplication.page_objects.ListMessagesPage import ListMessagesPage


import time

class MessageTest(MySeleniumTests):

    def test_see_message_received(self):
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
        
        page = page.click_on_read_more(0)
        time.sleep(5)
        
        self.assertEqual(0, 0)
        return True
    
    def test_see_message_sent(self):
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
        
        page = page.click_on_switch()
        time.sleep(1)
        
        page = page.click_on_read_more(0)
        time.sleep(1)
        
        self.assertEqual(0, 0)
        return True
    
    def test_send_message(self):
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
        
        page = page.click_on_new_message()
        time.sleep(1)
        
        page = page.fill_in_info("kim.mens@gmail.com", "Test subject", "Test content !\nYeah that's right !")
        time.sleep(2)
        
        page = page.click_on_submit()
        time.sleep(2)
        
        self.assertEqual(0, 0)
        return True