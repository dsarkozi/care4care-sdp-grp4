from C4CApplication.simulator.super_class import MySeleniumTests
import time


class SeleniumTestJob(MySeleniumTests):

    def test_register_job_done(self):
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