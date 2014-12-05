from C4CApplication.unit_tests.super_class import MySeleniumTests
from C4CApplication.page_objects.HomePage import HomePage

import time


class HelpedSimulation(MySeleniumTests):
    
    def test_simulation(self):
        self.populate_db()
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        
        """page = HomePage(self.selenium)
        page = page.click_on_sign_up() # Inscription page
        time.sleep(2)
        page = page.set_global_field('Marcel', 'Dupont', 'marcel_dupont@gmail.com', 'azertyuiop', 'M', '02',\
                         'septembre', '1990', 'Thatstreet', '7842', 'Thatcity', '010367309', '0477663691', [0], 0)
        time.sleep(2)
        page = page.click_on_submit()
        # registration done
        
        # back home
        time.sleep(2)
        page = page.click_home() # sachant que click_home ne renvoi pas HomePage
        """
        time.sleep(2)
        page = HomePage(self.selenium)
        page = page.login_successful("kim.mens@gmail.com","azertyuiop") # TODO set new email
        
        time.sleep(3)
        page = page.click_on_i_need_help() # CreateJobPage
        
        # page = page.put_job_offer_info
        # page.post
        
        # show how to accept a participation
        
        return True