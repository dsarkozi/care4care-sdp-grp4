from C4CApplication.simulator.super_class import MySeleniumTests
from selenium.webdriver.support.ui import Select
import time


class JobTest(MySeleniumTests):

    # test pour creer une demande de job (I need help)
    def offer_job_test(self):
        self.populate_db()
        
        # log in
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        time.sleep(1)
        username_input = self.selenium.find_element_by_name("email")
        username_input.send_keys('mathieu.jadin@student.uclouvain.be')
        time.sleep(1)
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('azertyuiop')
        time.sleep(1)
        self.selenium.find_element_by_xpath('//input[@value="Login"]').click()
        time.sleep(1)
        
        print("Logged for create job")
        
        # Test create job
        self.selenium.get('%s%s' % (self.live_server_url, '/newjob/demand'))
        time.sleep(1)
        title_input = self.selenium.find_element_by_name("title")
        title_input.send_keys('New demand test')
        time.sleep(1)
        desc_input = self.selenium.find_element_by_name("desc")
        desc_input.send_keys('Description of a demand test')
        time.sleep(1)
        # TODO aller voir select sur internet
        categories = self.selenium.find_element_by_name('categories')
        categories.click()
        time.sleep(1)
        
        frequency = self.selenium.find_element_by_name('frequency')
        frequency.click()
        time.sleep(1)
        
        month_select = Select(self.selenium.find_element_by_tag_name("select"))
        month_select.select_by_visible_text("March")
        time.sleep(1)
        
        subfrequency = self.selenium.find_element_by_name('subfrequency')
        subfrequency.click()
        time.sleep(1)
        
        visibility = self.selenium.find_element_by_name('visibility')
        visibility.click()
        time.sleep(1)
        # TODO idem pour 'frequency', 'subfrequency', 'weekdays', 'dayparts', 
        #'specific' and 'visibility'
        self.selenium.find_element_by_xpath('//input[@value="Post request"]').click()
        self.assertEqual(0, 0)
        return True
    
    def ask_for_help_test(self):
        self.populate_db()
        
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        
        self.assertEqual(0, 0)
        return True
    
    def accept_offer_test(self):
        self.populate_db()
        
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        
        self.assertEqual(0, 0)
        return True
    
    def accept_help_test(self):
        self.populate_db()
        
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        
        self.assertEqual(0, 0)
        return True

    def confirm_job_is_done_test(self):
        self.populate_db()
        
        # log in
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        time.sleep(1)
        username_input = self.selenium.find_element_by_name("email")
        username_input.send_keys('mathieu.jadin@student.uclouvain.be')
        time.sleep(1)
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('azertyuiop')
        time.sleep(1)
        self.selenium.find_element_by_xpath('//input[@value="Login"]').click()
        time.sleep(1)
        
        # Test confirm job
        self.selenium.get('%s%s' % (self.live_server_url, '/confirmjobdone/1'))
        time.sleep(1)
        job_time_input = self.selenium.find_element_by_name("time_to_pay")
        job_time_input.send_keys('40')
        time.sleep(1)
        self.selenium.find_element_by_xpath('//input[@value="Confirm"]').click()
        self.assertEqual(0, 0)
        return True
    
    def feeds_update_test(self):
        self.populate_db()
        
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        
        self.assertEqual(0, 0)
        return True
    
    def see_details_test(self):
        self.populate_db()
        
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        
        self.assertEqual(0, 0)
        return True
    
    def search_job_test(self):
        self.populate_db()
        
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        
        self.assertEqual(0, 0)
        return True