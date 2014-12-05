from C4CApplication.unit_tests.super_class import MySeleniumTests
from C4CApplication.page_objects.HomePage import HomePage
from C4CApplication.page_objects.MyCare4Care import MyCare4Care
from C4CApplication.page_objects.JobDetailsPage import JobDetailsPage

import time

# En gros c'est la petite vieille qui se fait tout le temps 
class HelpedSimulation(MySeleniumTests):
    
    def test_simulation_ask_help(self):
        # show how we can ask for help
        self.populate_db()
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        time.sleep(2)
        
        page = HomePage(self.selenium)
        # si le click bug -> aller dans homepage et changer le nom
        page = page.click_on_sign_up() # Inscription page
        time.sleep(2)
        page = page.set_global_field('Janine', 'cougnou', 'janine_kou@gmail.com', 'azertyuiop', 'F', '16',\
                         'juillet', '1940', 'Anotherstreet', '7842', 'Thatcity', '010377355', '0470698621', [0], 1)
        time.sleep(2)
        page = page.click_on_submit()
        # registration done
        
        time.sleep(2)
        page = HomePage(self.selenium)
        page = page.login_successful("janine_kou@gmail.com","azertyuiop") 
        
        time.sleep(3)
        page = page.click_on_i_need_help() # CreateJobPage
        time.sleep(2)
        
        # Test create job
        page = page.create_job("I need help", "I need help for bringing me to the shop", "From my place to the shop", 0, "10:30", \
                               "01:00", "10", 0, 1, "", "", "", [2, 5], [], [0], True)
        # page.post
        page = page.click_on_post_req() # on arrive sur myc4c
        time.sleep(1)
        
        page = MyCare4Care(self.selenium)
        page.log_out()
        
        return True
    
    def test_simulation_accept_participation(self):
        # show how to accept a participation
        self.populate_db()
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        time.sleep(2)
        
        # login
        page = HomePage(self.selenium)
        # the test fails if janine is not in the DB
        page = page.login_successful("janine_kou@gmail.com","azertyuiop") 
        time.sleep(1)
        
        page = page.click_home()
        time.sleep(1)
        page = HomePage(self.selenium)
        
        page = page.click_on_last_offer() # JobDetailsPage
        time.sleep(1)
        
        page = page.click_on_choose_member(0)
        time.sleep(1)
        
        # logout
        page = page.click_home()
        time.sleep(1)
        page = HomePage(self.selenium)
        page = page.click_on_logout
        
        return True
    
    def test_simulation_complaint_theft(self):
        # la vieille se log in
        
        # click on branchlist
        
        # click on my branch
        
        # click on branch officer
        
        # send mail to branch officer about the theft
        
        # log out
        return True
