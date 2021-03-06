from C4CApplication.page_objects.FixedPage import FixedPage


class ConfirmJobDonePage(FixedPage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.job_time_input = self.driver.find_element_by_name("time_to_pay")
        self.confirm_button = self.driver.find_element_by_xpath('//input[@id="Confirm"]')
        
    def enter_time_to_pay(self, time):
        self.job_time_input.send_keys(str(time))
        return self
        
    def click_on_confirm(self):
        self.confirm_button.click()
        #return HomePage(driver)