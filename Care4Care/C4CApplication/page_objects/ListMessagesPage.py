from C4CApplication.page_objects.MyCare4CarePage import MyCare4CarePage
from selenium.webdriver.common.by import By


class ListMessagesPage(MyCare4CarePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.switch_button = None
        self.new_message_button = None 
        self.read_more_buttons = None