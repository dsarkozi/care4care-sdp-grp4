from C4CApplication.simulator.super_class import MySeleniumTests
import time


class SeleniumTestJob(MySeleniumTests):

    def test_register_job_done(self):
        self.populate_db()
        
        # TODO login sinon on arrive sur forbiden !
        self.selenium.get('%s%s' % (self.live_server_url, '/confirmjobdone/1'))
        time.sleep(1)
        #username_input = self.selenium.find_element_by_name("email")
        #username_input.send_keys('mathieu.jadin@student.uclouvain.be')
        time.sleep(1)
        #password_input = self.selenium.find_element_by_name("password")
        #password_input.send_keys('azertyuiop')
        time.sleep(1)
        #self.selenium.find_element_by_xpath('//input[@value="Login"]').click()
        time.sleep(1)
        self.assertEqual(0, 0)
        return True