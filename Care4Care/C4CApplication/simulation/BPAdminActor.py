from C4CApplication.page_objects.BranchListPage import BranchListPage
from C4CApplication.page_objects.CreateBranchPage import CreateBranchPage
from C4CApplication.page_objects.FixedPage import FixedPage
from C4CApplication.simulation.Actor import Actor

from C4CApplication.page_objects.HomePage import HomePage
from C4CApplication.page_objects.MyCare4Care import MyCare4Care

import time


class BPAdminActor(Actor):
    """
    This class represents a bp administrator that will do some actions
    """

    action_list = None

    def get_action_list(self):

        if self.action_list is None:
            self.action_list = [
                [self.login_action, self.test_create_branch, self.logout_action]
            ]

        return self.action_list

    def remove_action_from_action_list(self, action):
        self.action_list.remove(action)

    @staticmethod
    def login_action(selenium, live_server_url):
        """
        Login the actor
        :param selenium: The instance of selenium
        :param live_server_url:
        :return: True if the action was successfull,
                 False if the action is impossible now but perhaps could be performed in the future
                 None if the action failed unexcpectedly
        """

        selenium.get('%s%s' % (live_server_url, ''))  # Go to the home page

        time.sleep(2)
        page = HomePage(selenium)
        page.login_successful("mathieu.jadin@student.uclouvain.be", "azertyuiop")  # Kim is branch officer of LLN
        time.sleep(2)

        return True

    @staticmethod
    def test_create_branch(selenium, live_server_url):
        """
        Creates a new branch and put himself as a branch officer
        :return: True if the action was successfull,
                 False if the action is impossible now but perhaps could be performed in the future
                 None if the action failed unexcpectedly
        """
        page = MyCare4Care(selenium)
        page.BP_click_on_new_branch()

        page = CreateBranchPage(selenium)
        time.sleep(2)

        page = page.fill_in_info('Bxl', 'Bruxelles-Molenbeek', 'mathieu.jadin@student.uclouvain.be', "Rue de la Reussite 42", "7652", "Bruxelles")
        time.sleep(3)

        page = page.click_on_submit()
        time.sleep(2)

        return True


    @staticmethod
    def logout_action(selenium, live_server_url):
        """
        Logout the actor
        :param selenium: The instance of selenium
        :param live_server_url:
        :return: True if the action was successfull,
                 False if the action is impossible now but perhaps could be performed in the future
                 None if the action failed unexcpectedly
        """

        # Go to home page
        page = MyCare4Care(selenium)
        time.sleep(2)
        page.click_home()
        time.sleep(2)

        # Logout
        page = HomePage(selenium)
        page.click_on_logout()
        time.sleep(2)

        return True