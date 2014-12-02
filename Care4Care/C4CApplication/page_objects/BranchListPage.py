from C4CApplication.page_objects.FixedPage import FixedPage
from selenium.webdriver.common.by import By

import time


class BranchListPage(FixedPage):
    
    def __init__(self, driver):
        super().__init__(driver)