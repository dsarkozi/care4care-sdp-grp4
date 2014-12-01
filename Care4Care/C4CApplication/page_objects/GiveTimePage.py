from C4CApplication.page_objects.Page import Page
from C4CApplication.page_objects.MyCare4Care import MyCare4Care
from selenium.webdriver.common.by import By

import time


class GiveTimePage(Page):
    
    def __init__(self, driver):
        super().__init__(driver)
        
    