from C4CApplication.page_objects.HomePage import HomePage
from C4CApplication.page_objects.MyCare4Care import MyCare4Care
from C4CApplication.simulation.Actor import Actor

import time


class HelperActor(Actor):
    """
    This class represents a helper that will do some actions
    """

    action_list = None

    def get_action_list(self):

        if self.action_list is None:
            self.action_list = [
                [self.login_action, self.logout_action]
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
        page.login_successful("kim.mens@gmail.com", "azertyuiop")  # TODO -> change to Janine

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
        time.sleep(2)
        page.click_on_logout()
        time.sleep(2)

        return True