from C4CApplication.page_objects.FixedPage import FixedPage


class JobDetailsPage(FixedPage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.choose_member_buttons = None
        self.delete_job_button     = None
        self.participate_button    = None
        try : self.delete_job_button = self.driver.find_elements_by_xpath('//a[@id="delete_job"]')
        except : pass
        try : self.choose_member_buttons = self.driver.find_elements_by_xpath("//a[@id='choose_this_member']")
        except : pass
        try : self.participate_button = self.driver.find_element_by_xpath('//a[@id="participate_button"]')
        except : pass

    def click_on_logout(self):
        self.driver.find_element_by_xpath('//a[@value="Logout"]').click()
        return self

    def click_on_participate(self):
        if self.participate_button is not None: 
            self.participate_button.click()
        return self
    
    def click_on_choose_member(self, num):
        if num < len(self.choose_member_buttons): 
            self.choose_member_buttons[num].click()
        else: 
            print("No enough member to choose (num < size of choose_member_buttons)")
        return self