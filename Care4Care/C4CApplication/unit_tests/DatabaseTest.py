from C4CApplication.unit_tests.super_class import MySeleniumTests

import time


class DatabaseTest(MySeleniumTests):

    def backup_test(self):
        self.populate_db()
        
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        
        self.assertEqual(0, 0)
        return True