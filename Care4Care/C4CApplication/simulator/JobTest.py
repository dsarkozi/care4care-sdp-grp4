from C4CApplication.simulator.super_class import MySeleniumTests
from selenium.webdriver.support.ui import Select
from C4CApplication.page_objects.CreateJobPage import CreateJobPage
import time


class JobTest(MySeleniumTests):

    # test pour creer une demande de job (I need help)
    def test_offer_job(self):
        self.populate_db()
        
        # log in
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        username_input = self.selenium.find_element_by_name("email")
        username_input.send_keys('mathieu.jadin@student.uclouvain.be')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('azertyuiop')
        self.selenium.find_element_by_xpath('//input[@value="Login"]').click()
        
        self.selenium.get('%s%s' % (self.live_server_url, '/newjob/demand'))
        page = CreateJobPage(self.selenium)
        
        print("Page object created")
        # Test create job
        page = page.create_job_offer("New offer title", "New offer description", "Visit", "Only once", 
                         "March", "Specific day", "Anyone")
        
        print("Job created")
        #page = page.click_on_post_req()
        
        print("Done")
        
        self.assertEqual(0, 0)
        return True
    
    """def ask_for_help_test(self):
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
        return True"""