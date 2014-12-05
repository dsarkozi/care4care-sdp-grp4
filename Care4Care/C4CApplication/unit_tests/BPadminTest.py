from C4CApplication.unit_tests.super_class import MySeleniumTests
#from C4CApplication.page_objects.HomePage import HomePage
from C4CApplication.page_objects.CreateBranchPage import CreateBranchPage
from C4CApplication.page_objects.TransferRightsBranchPage import TransferRightsBranchPage
from C4CApplication.page_objects.TransferRightsPage import TransferRightsPage

from C4CApplication.models import Branch
from C4CApplication.models import Member

import time


class BPadminTest(MySeleniumTests):

    def test_create_branch(self):
        self.populate_db()
        
        # log in
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        username_input = self.selenium.find_element_by_name("email")
        username_input.send_keys('mathieu.jadin@student.uclouvain.be')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('azertyuiop')
        self.selenium.find_element_by_xpath('//input[@value="Login"]').click()
        time.sleep(1)
        
        self.selenium.get('%s%s' % (self.live_server_url, '/createbranch/'))
        time.sleep(1)
        
        page = CreateBranchPage(self.selenium)
        time.sleep(2)
        
        page = page.fill_in_info('Bxl', 'Bruxelles-Molenbeek', 'mathieu.jadin@student.uclouvain.be', "Rue de la Reussite 42", "7652", "Bruxelles")
        time.sleep(2)
        
        page = page.click_on_submit()
        time.sleep(2)
        
        branch = Branch.objects.filter(name='Bxl')
        self.assertEqual(len(branch), 1)
        branch=branch[0]
        self.assertEqual(branch.branch_town, 'Bruxelles-Molenbeek')
        self.assertEqual(branch.branch_officer, 'mathieu.jadin@student.uclouvain.be')
        self.assertEqual(branch.street, 'Rue de la Reussite 42')
        self.assertEqual(branch.zip, "7652")
        self.assertEqual(branch.town, "Bruxelles")
        return True

    
    def test_change_branch_officer(self):
        self.populate_db()

        # log in
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        username_input = self.selenium.find_element_by_name("email")
        username_input.send_keys('mathieu.jadin@student.uclouvain.be')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('azertyuiop')
        self.selenium.find_element_by_xpath('//input[@value="Login"]').click()
        time.sleep(1)
        
        self.selenium.get('%s%s' % (self.live_server_url, '/transferrightsbranch/LLN/'))
        time.sleep(1)
        
        page = TransferRightsBranchPage(self.selenium)
        page = page.set_email_new_branch_off("kim.mens@gmail.com")
        time.sleep(2)
        
        page = page.click_on_change()
        time.sleep(1)
        
        branch = Branch.objects.filter(name='LLN')
        self.assertEqual(len(branch), 1)
        branch=branch[0]
        self.assertEqual(branch.branch_officer, 'kim.mens@gmail.com')
        return True
    
    def test_resing_from_bp_admin(self):
        self.populate_db()

        # log in
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        username_input = self.selenium.find_element_by_name("email")
        username_input.send_keys('mathieu.jadin@student.uclouvain.be')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('azertyuiop')
        self.selenium.find_element_by_xpath('//input[@value="Login"]').click()
        time.sleep(1)
        
        self.selenium.get('%s%s' % (self.live_server_url, '/transferrights/'))
        time.sleep(1)
        
        page = TransferRightsPage(self.selenium)
        page = page.set_email_new_bpa("kim.mens@gmail.com")
        time.sleep(2)
        
        page = page.click_on_change()
        time.sleep(2)
        
        oldBP = Member.objects.filter(mail='mathieu.jadin@student.uclouvain.be')
        self.assertEqual(len(oldBP), 1)
        oldBP = oldBP[0]
        newBP = Member.objects.filter(mail='kim.mens@gmail.com')
        self.assertEqual(len(newBP), 1)
        newBP = newBP[0]
        self.assertEqual(oldBP.tag, 12)
        self.assertEqual(newBP.tag, 32)
        return True