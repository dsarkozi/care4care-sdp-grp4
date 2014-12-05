from C4CApplication.unit_tests.super_class import MySeleniumTests
from C4CApplication.page_objects.HomePage import HomePage

import time


class HelperSimulation(MySeleniumTests):
    
    def test_simulation(self):
        self.populate_db()
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        
        """page = HomePage(self.selenium)
        page = page.click_on_sign_up() # Inscription page
        time.sleep(2)
        page = page.set_global_field('Marcel', 'Dupont', 'marcel_dupont@gmail.com', 'azertyuiop', 'M', '02',\
                         'septembre', '1990', 'Thatstreet', '7842', 'Thatcity', '010367309', '0477663691', [0], 1)
        time.sleep(2)
        page = page.click_on_submit()
        # registration done
        
        # back home
        time.sleep(2)
        page = page.click_home() # sachant que click_home ne renvoi pas HomePage
        """
        time.sleep(2)
        page = HomePage(self.selenium)
        page = page.login_successful("kim.mens@gmail.com","azertyuiop")  # TODO set new email
        
        time.sleep(3)
        page = page.click_on_i_want_to_help()  # CreateJobPage
        
        # Test create job
        page = page.create_job("I want to help for ...", "I provide my help for bringing someone to the shop", "From your place to the shop", 0, "10:30", \
                               "01:00", "10", 0, 1, "", "", "", [2, 5], [], [0], True)
        # page.post
        
        
        return True
    
    def test_simulation_participate(self):
        # maybe show how to select a job offer and participate
        return True