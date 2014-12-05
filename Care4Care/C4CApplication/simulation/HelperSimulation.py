from C4CApplication.unit_tests.super_class import MySeleniumTests
from C4CApplication.page_objects.HomePage import HomePage
from C4CApplication.page_objects.MyCare4Care import MyCare4Care

import time


class HelperSimulation(MySeleniumTests):
    
    def test_simulation_offer_help(self):
        self.populate_db()
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        time.sleep(2)
        
        page = HomePage(self.selenium)
        page = page.click_on_sign_up() # Inscription page
        time.sleep(2)
        page = page.set_global_field('Marcel', 'Dupont', "marcel_dupont@gmail.com", 'azertyuiop', 'M', '4',\
                         'septembre', '1990', 'Thatstreet', '7842', 'Thatcity', '010367309', '0477663691', [0], 1)
        time.sleep(2)
        page = page.click_on_submit()
        # registration done
  
        time.sleep(2)
        page = HomePage(self.selenium)
        page = page.login_successful("marcel_dupont@gmail.com","azertyuiop") # TODO set new email
        
        time.sleep(3)
        page = page.click_on_i_want_to_help() # CreateJobPage
        time.sleep(1)
        
        # Test create job
        page = page.create_job("I want to help for ...", "I provide my help for bringing someone to the shop", "From your place to the shop", 0, "10:30", \
                               "01:00", "10", 0, 1, "", "", "", [2, 5], [], [0], True)
       
        # Post
        page = page.click_on_post_req() # on arrive sur myc4c
        time.sleep(1)
        
        page = MyCare4Care(self.selenium)
        page.log_out()
        
        return True
    
    def test_simulation_participate(self):
        # show how to select a job offer and participate
        self.populate_db()
        self.selenium.get('%s%s' % (self.live_server_url, ''))
  
        # login
        page = HomePage(self.selenium)
        # the test fails if marcel is not in the DB
        page = page.login_successful("marcel_dupont@gmail.com","azertyuiop") 
        time.sleep(1)
        
        page = page.click_home()
        time.sleep(1)
        page = HomePage(self.selenium)
        
        # click on a job demand
        page = page.click_on_last_demand() # JobDetailsPage
        
        # click on participate
        page = page.click_on_participate()
        
        # log out
        page = page.click_on_logout()
        
        return True