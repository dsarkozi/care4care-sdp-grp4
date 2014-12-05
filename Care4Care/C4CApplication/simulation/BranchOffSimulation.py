from C4CApplication.unit_tests.super_class import MySeleniumTests
from C4CApplication.page_objects.HomePage import HomePage

import time


class BranchOffSimulation(MySeleniumTests):
    
    def test_simulation(self):
        self.populate_db()
        self.selenium.get('%s%s' % (self.live_server_url, ''))

        time.sleep(2)
        page = HomePage(self.selenium)
        page = page.login_successful("kim.mens@gmail.com","azertyuiop") # kim is branch off of lln
        
        time.sleep(3)
        #page = page.
        
        # click on branches 
        # click on lln
        #page = page.click_on_branch_details(0) # ne renvoie pas la page suivante
        
        # click on a member 
        # TODO MemberListPage il manque les liens des gens
        
        # click on log as member 
        #page = page.click_on_log_as_member() # ne renvoie pas la page suivante
        
        return True