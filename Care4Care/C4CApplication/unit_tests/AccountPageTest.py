from C4CApplication.unit_test.super_class import MySeleniumTests


import time

""" Test inutile ? -> on fais ca dans les test de db """
class AccountPageTest(MySeleniumTests):

    def see_pending_jobs_test(self):
        self.populate_db()
        
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        
        self.assertEqual(0, 0)
        return True
    
    def statistics_time_test(self):
        '''
        Optionnel je crois
        '''
        pass
    
    def statistic_jobs_done_test(self):
        '''
        Optionnel aussi je crois
        '''
        pass
    
    def see_account_balance_test(self):
        self.populate_db()
        
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        
        self.assertEqual(0, 0)
        return True