from C4CApplication.unit_tests.super_class import MySeleniumTests
from C4CApplication.page_objects.HomePage import HomePage

import time


class HelpedSimulation(MySeleniumTests):
    
    def test_simulation_ask_help(self):
        self.populate_db()
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        
        """page = HomePage(self.selenium)
        page = page.click_on_sign_up() # Inscription page
        time.sleep(2)
        page = page.set_global_field('Janine', 'Kouniou', 'janine_kou@gmail.com', 'azertyuiop', 'F', '16',\
                         'juillet', '1940', 'Anotherstreet', '7842', 'Thatcity', '010377355', '0470698621', [0], 1)
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
        time.sleep(2)
        
        # Test create job
        page = page.create_job("I need help", "I need help for bringing me to the shop", "From my place to the shop", 0, "10:30", \
                               "01:00", "10", 0, 1, "", "", "", [2, 5], [], [0], True)
        # page.post
        
        # TODO
        
        #page = page.click_home()
        #page = HomePage(self.selenium)
        #page.click_on_logout()
        print("FIN de la simulation !")
        
        return True
    
    def test_simulation_accpet_participation(self):
        # show how to accept a participation
        self.populate_db()
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        
        # voir choose this member 
        # TODO
        
        return True
        