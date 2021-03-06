import time

from C4CApplication.unit_tests.super_class import MySeleniumTests
from C4CApplication.page_objects.BranchListPage import BranchListPage
from C4CApplication.page_objects.HomePage import HomePage
from C4CApplication.models.branch import Branch


class BranchTest(MySeleniumTests):

    def test_join_branch(self):
        self.populate_db()
        
        # log in
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        page = HomePage(self.selenium)
        page = page.quick_login_successful('mathieu.jadin@student.uclouvain.be', 'azertyuiop')
        time.sleep(1)
        
        self.selenium.get('%s%s' % (self.live_server_url, '/branchlist'))
        page = BranchListPage(self.selenium)
        time.sleep(1)
        
        page.click_on_new_branch(1)
        time.sleep(1)
        
        page = page.click_on_submit()
        time.sleep(1)
        
        branch = Branch.objects.filter(name="Nivelles")
        self.assertEqual(len(branch),1)
        branch = branch[0]
        bool = False
        for mem in branch.member_set.all():
            if mem.mail == 'mathieu.jadin@student.uclouvain.be' :
                bool=True
        self.assertEqual(bool, True)
        return True