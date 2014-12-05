from C4CApplication.unit_tests.super_class import MySeleniumTests
from C4CApplication.page_objects.HomePage import HomePage
from C4CApplication.page_objects.BranchListPage import BranchListPage
from C4CApplication.page_objects.MyCare4Care import MyCare4Care


import time


class BranchOffSimulation(MySeleniumTests):
    
    def test_simulation(self):
        self.populate_db()
        self.selenium.get('%s%s' % (self.live_server_url, ''))

        time.sleep(2)
        page = HomePage(self.selenium)
        page = page.login_successful("kim.mens@gmail.com", "azertyuiop")  # Kim is branch officer of LLN
        
        time.sleep(3)
        page = page.click_on_care4care_branches()  # click on branches
        time.sleep(1)
        page = BranchListPage(self.selenium)
        page = page.click_on_branch_details(0)  # click on lln -> MemberListPage
        time.sleep(1)
        
        page = page.click_on_member(1)  # click on a member -> MemberDetailsPage
        time.sleep(1)
        page = page.click_on_log_as_member()  # log as the member
        time.sleep(1)
        
        page = MyCare4Care(self.selenium)
        #page = page.click_on_i_need_help() # create help demand
        time.sleep(1)
        
        # reprendre etapes de helpedsimulation
        
        page = page.click_home()
        page = HomePage(self.selenium)
        page.click_on_logout()
        print("FIN de la simulation !")
                
        return True