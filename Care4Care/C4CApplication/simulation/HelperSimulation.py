from C4CApplication.unit_test.super_class import MySeleniumTests
from C4CApplication.page_objects.HomePage import HomePage

class HelperSimulation(MySeleniumTests):
    
    def test_simulation(self):
        print("Coucou")