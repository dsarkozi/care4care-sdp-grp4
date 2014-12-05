from C4CApplication.unit_tests.super_class import MySeleniumTests
from C4CApplication.page_objects.HomePage import HomePage
from C4CApplication.page_objects.BranchListPage import BranchListPage
from C4CApplication.page_objects.MemberListPage import MemberListPage
from C4CApplication.page_objects.InscriptionPage import InscriptionPage
from C4CApplication.page_objects.ProfilePage import ProfilePage
from C4CApplication.page_objects.ModifProfilePage import ModifProfilePage
from C4CApplication.models.member import Member


import time


class UserAccountTest(MySeleniumTests):
    
    def test_login(self):
        self.populate_db()
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        
        home_page = HomePage(self.selenium)
        home_page.login_successful('mathieu.jadin@student.uclouvain.be', 'azertyuiop')
        time.sleep(1)
        
        name = self.selenium.find_elements_by_xpath("//span[@class='nom']")[0]
        self.assertEqual(name.text, "Mathieu Jadin")
        return True
        
        
    def test_logoff(self):
        self.populate_db()
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        page = HomePage(self.selenium)
        page = page.quick_login_successful('olivier.mauvaisaventure@gmail.com', 'azertyuiop')
        time.sleep(1)
        
        page.log_out()
        time.sleep(1)
        
        login = self.selenium.find_elements_by_xpath("//input[@type='submit']")[0]
        self.assertEqual(login.is_displayed(), True)
        return True
    
    def test_create_member_account(self):
        self.populate_db()
        
        # log in
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        time.sleep(1)
        self.selenium.find_element_by_xpath('//input[@value="Sign up"]').click()
        time.sleep(3)
        
        page = InscriptionPage(self.selenium)
        page = page.set_global_field('Mister', 'Nobody', 'mister_nobody@gmail.com', 'azertyuiop', 'M', '14',\
                         'juin', '1920', 'Multilife', '6458', 'Nivelles', '010564339', '0477662396', [0, 1], 0)
        time.sleep(1)
        
        page = page.click_on_submit()
        time.sleep(5)
        
        
        self.assertEqual(0, 0)
        return True
    
    def test_delete_account(self):
        self.populate_db()
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        page = HomePage(self.selenium)
        page = page.quick_login_successful('dr.robotnik@gmail.com', 'azertyuiop')
        time.sleep(1)
        
        page = ProfilePage(self.selenium)
        page.click_on_modif_profile()
        time.sleep(1)
        
        page = ModifProfilePage(self.selenium)
        page.click_on_delete_account()
        time.sleep(1)
        
        page = HomePage(self.selenium)
        page = page.login_fail('dr.robotnik@gmail.com', 'azertyuiop')
        time.sleep(3)
        
        members = Member.objects.filter(mail="dr.robotnik@gmail.com")
        self.assertEqual(len(members), 1)
        self.assertEqual(members[0].deleted, True)
        return True
    
    def test_update_to_volunteer(self):
        self.populate_db()
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        page = HomePage(self.selenium)
        page = page.quick_login_successful('kim.mens@gmail.com', 'azertyuiop')
        time.sleep(1)
        
        page.click_on_care4care_branches()
        page = BranchListPage(self.selenium)
        time.sleep(1)
        
        page.click_on_branch_details(0)
        page = MemberListPage(self.selenium)
        time.sleep(1)
        
        page.click_on_promote_volunteer(0)
        time.sleep(2)
        
        member = Member.objects.filter(mail="olivier.mauvaisaventure@gmail.com")
        self.assertEqual(len(member), 1)
        self.assertEqual(member[0].tag, 8)
        return True
