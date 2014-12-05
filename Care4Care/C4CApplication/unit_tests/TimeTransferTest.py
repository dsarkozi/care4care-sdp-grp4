from C4CApplication.unit_tests.super_class import MySeleniumTests
from C4CApplication.page_objects.HomePage import HomePage
from C4CApplication.page_objects.GiveTimePage import GiveTimePage
from C4CApplication.models import Member


import time


class TimeTransferTest(MySeleniumTests):
    
    def test_donation(self):
        #login
        self.populate_db()
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        page = HomePage(self.selenium)
        page = page.quick_login_successful('mathieu.jadin@student.uclouvain.be', 'azertyuiop')
        time.sleep(1)
        
        # Get time account before donation
        giver = Member.objects.filter(mail='mathieu.jadin@student.uclouvain.be')
        if len(giver) == 1: giver = giver[0]
        else: self.assertEqual(0, 1) # end the test
        time_account_before = giver.time_credit
        print("Time credits before : "+str(time_account_before))
        
        self.selenium.get('%s%s' % (self.live_server_url, '/donate/'))
        time.sleep(1)
        
        page = GiveTimePage(self.selenium)
        time.sleep(1)
        
        page = page.fill_in_fields("Voici un peu de temps", "1", "3", "0", "Care4Care compagny")
        time.sleep(1)
        
        page = page.click_on_donate()
        time.sleep(2)
        
        # Get time account after donation
        giver = Member.objects.filter(mail='mathieu.jadin@student.uclouvain.be')
        if len(giver) == 1: giver = giver[0]
        else: self.assertEqual(0, 1) # end the test
        time_account_after = giver.time_credit
        print("Time credits after : "+str(time_account_after))
        
        self.assertEqual(time_account_before, time_account_after+1620)
        return True
    
    def test_gift(self):
        #login
        self.populate_db()
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        page = HomePage(self.selenium)
        page = page.quick_login_successful('mathieu.jadin@student.uclouvain.be', 'azertyuiop')
        time.sleep(1)
        
        self.selenium.get('%s%s' % (self.live_server_url, '/donate/'))
        time.sleep(1)
        
        page = GiveTimePage(self.selenium)
        time.sleep(3)
        
        page = page.fill_in_fields("Tiens Olivier, voici du temps ;)", "0", "1", "40", "Olivier", 1)
        time.sleep(2)
        
        page = page.click_on_donate()
        
        self.assertEqual(0, 0)
        return True