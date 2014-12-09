from C4CApplication.unit_tests.super_class import MySeleniumTests
from C4CApplication.page_objects.ModifProfilePage import ModifProfilePage
from C4CApplication.page_objects.HomePage import HomePage
from C4CApplication.models.member import Member


import time


class ProfileTest(MySeleniumTests):

    # database test
    """def see_data_test(self):
        self.populate_db()
        
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        
        self.assertEqual(0, 0)
        return True"""
    
    def test_update_data(self):
        #log in
        self.populate_db()
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        time.sleep(1)
        
        page = HomePage(self.selenium)
        page = page.quick_login_successful('olivier.mauvaisaventure@gmail.com', 'azertyuiop')
        time.sleep(1)
        
        self.selenium.get('%s%s' % (self.live_server_url, '/modifprofile/'))
        time.sleep(1)
        
        page = ModifProfilePage(self.selenium)
        page = page.fill_in_info("Rue bidon, 15", "9999", "Bouseville", "010010010", "0456880045")
        time.sleep(1)
        
        page = page.click_on_submit()
        time.sleep(1)
        
        olivier = Member.objects.filter(mail='olivier.mauvaisaventure@gmail.com')
        self.assertEqual(len(olivier),1)
        olivier = olivier[0]
        self.assertEqual(olivier.street, "Rue bidon, 15")
        self.assertEqual(olivier.zip, "9999")
        self.assertEqual(olivier.town, "Bouseville")
        self.assertEqual(olivier.telephone, "010010010")
        self.assertEqual(olivier.mobile, "0456880045")
        return True
    
    def test_delete_picture(self):
        #log in
        self.populate_db()
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        time.sleep(1)
        
        page = HomePage(self.selenium)
        page = page.quick_login_successful('mathieu.jadin@student.uclouvain.be', 'azertyuiop')
        time.sleep(1)
        
        self.selenium.get('%s%s' % (self.live_server_url, '/modifprofile/'))
        time.sleep(1)
        
        page = ModifProfilePage(self.selenium)
        page = page.click_on_delete_picture()
        time.sleep(1)
        
        
        mathieu = Member.objects.filter(mail='mathieu.jadin@student.uclouvain.be')
        self.assertEqual(len(mathieu), 1)
        mathieu = mathieu[0]
        self.assertEqual(mathieu.picture, "")
        return True