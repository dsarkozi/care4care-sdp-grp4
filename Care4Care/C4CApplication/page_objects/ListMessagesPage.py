from C4CApplication.page_objects.FixedPage import FixedPage
from selenium.webdriver.common.by import By


class ListMessagesPage(FixedPage):
    
    def __init__(self, driver):
        self.driver = driver # TODO
        buttons = self.driver.find_elements_by_xpath('//a[@class="btn"]') # all elements of the class "btn"
        
        self.switch_button = None
        self.new_message_button = None
        self.read_more_buttons = []
        
        for el in buttons: # maybe change this if the language change
            print(el.text)
            if el.text.startswith('Switch') : 
                self.switch_button = el
            elif el.text.startswith('Write') :
                self.new_message_button = el
            elif el.text.startswith('Read') :
                self.read_more_buttons.append(el)
        #self.new_message_button = self.driver.find_element_by_xpath('//a[@value="new_message"]') 
        
    def click_on_read_more(self, num):
        if len(self.read_more_buttons) < num+1:
            print("No such a message : \nAre you sure that at least "+str((num+1))+" messages have been received ?")
            return self
        
        self.read_more_buttons[num].click()
        return self
    
    def click_on_new_message(self):
        self.new_message_button.click()
        return self
    
    def click_on_switch(self):
        if self.switch_button is not None: 
            self.switch_button.click()
        else: print("Switch button not found !")
        return ListMessagesPage(self.driver)