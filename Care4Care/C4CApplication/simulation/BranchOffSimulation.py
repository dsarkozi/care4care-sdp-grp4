from C4CApplication.unit_tests.super_class import MySeleniumTests
from C4CApplication.page_objects.HomePage import HomePage
from C4CApplication.page_objects.BranchListPage import BranchListPage

import time


class BranchOffSimulation(MySeleniumTests):
    
    def test_simulation(self):
        self.populate_db()
        self.selenium.get('%s%s' % (self.live_server_url, ''))

        time.sleep(2)
        page = HomePage(self.selenium)
        page = page.login_successful("kim.mens@gmail.com","azertyuiop") # kim is branch off of lln
        
        time.sleep(3)
        page = page.click_on_care4care_branches() # click on branches
        time.sleep(1)
        page = BranchListPage(self.selenium)
        page = page.click_on_branch_details(0) # click on lln -> MemberListPage
        time.sleep(1)
        
        page = page.click_on_member(1) # click on a member -> MemberDetailsPage
        time.sleep(1)
        page = page.click_on_log_as_member() # log as the member 
        time.sleep(1)
                
        return True