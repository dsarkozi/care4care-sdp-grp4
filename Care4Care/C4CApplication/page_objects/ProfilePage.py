from C4CApplication.page_objects.MyCare4CarePage import MyCare4CarePage
from selenium.webdriver.common.by import By


class ProfilePage(MyCare4CarePage):
    self.browse_button = None
    self.delete_pic_button = None
    self.street_input = None
    self.number_input = None
    self.postal_code_input = None
    self.town_input = None
    self.phone_num_input = None
    self.mobile_phone_input = None
    