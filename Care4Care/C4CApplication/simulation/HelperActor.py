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
                [self.sign_up_action, self.login_action, self.logout_action]
            ]

        return self.action_list

    def remove_action_from_action_list(self, action):
        self.action_list.remove(action)

    @staticmethod
    def sign_up_action(selenium, live_server_url):
        """
        Sign up the actor
        :param selenium: The instance of selenium
        :param live_server_url:
        :return: True if the action was successfull,
                 False if the action is impossible now but perhaps could be performed in the future
                 None if the action failed unexcpectedly
        """

        selenium.get('%s%s' % (live_server_url, ''))  # Go to the home page

        page = HomePage(selenium)

        page = page.click_on_sign_up()  # Inscription page
        time.sleep(2)
        page = page.set_global_field('Marcel', 'Dupont', "marcel_dupont@gmail.com", 'azertyuiop', 'M', '4',
                         'septembre', '1990', 'Thatstreet', '7842', 'Thatcity', '010367309', '0477663691', [0], 1)
        time.sleep(2)
        page = page.click_on_submit()
        # registration done

        time.sleep(2)

        return True


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
        page.login_successful("marcel_dupont@gmail.com", "azertyuiop")

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