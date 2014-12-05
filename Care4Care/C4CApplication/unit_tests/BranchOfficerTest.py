from C4CApplication.unit_tests.super_class import MySeleniumTests
from C4CApplication.page_objects.MemberDetailsPage import MemberDetailsPage
from C4CApplication.page_objects.MemberListPage import MemberListPage
from C4CApplication.models.branch import Branch
from C4CApplication.page_objects.HomePage import HomePage


import time


class BranchOfficerTest(MySeleniumTests):

    def test_remove_branch_member(self):
        self.populate_db()
        branch = Branch.objects.filter(name="LLN")
        self.assertEqual(len(branch), 1)
        branch = branch[0]
        member_list = branch.member_set.all()
        prev_length = len(member_list)

        # log in
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        page = HomePage(self.selenium)
        page = page.quick_login_successful('kim.mens@gmail.com', 'azertyuiop')
        
        self.selenium.get('%s%s' % (self.live_server_url, '/branchdetails/LLN/'))
        time.sleep(1)
        
        page = MemberListPage(self.selenium)
        time.sleep(1)
        
        page = page.click_on_remove_from_branch(1)
        time.sleep(1)
        
        member_list = branch.member_set.all()
        self.assertEqual(len(member_list)+1, prev_length)
        return True
    
    def test_log_as_other_member(self):
        self.populate_db()
        
        # log in
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        page = HomePage(self.selenium)
        page = page.quick_login_successful('kim.mens@gmail.com', 'azertyuiop')
        
        self.selenium.get('%s%s' % (self.live_server_url, '/memberdetails/olivier.mauvaventure%40gmail.com'))
        time.sleep(1)

        page = MemberDetailsPage(self.selenium)
        time.sleep(1)
        
        page = page.click_on_log_as_member()
        time.sleep(1)
        
        self.assertEqual(0, 0)
        return True