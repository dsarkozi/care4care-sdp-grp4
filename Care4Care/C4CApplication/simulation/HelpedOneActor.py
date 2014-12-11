import time

from C4CApplication.simulation.Actor import Actor
from C4CApplication.page_objects.HomePage import HomePage
from C4CApplication.page_objects.MyCare4Care import MyCare4Care


class HelpedOneActor(Actor):
    """
    This class represents a member that will do some actions to ask for help
    """

    action_list = None

    def get_action_list(self):

        if self.action_list is None:
            self.action_list = [
                [self.sign_up_action, self.login_action, self.create_job_action, self.logout_action]
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
        # si le click bug -> aller dans homepage et changer le nom
        page = page.click_on_sign_up()  # Inscription page
        time.sleep(2)
        page = page.set_global_field('Janine', 'cougnou', 'janine_kou@gmail.com', 'azertyuiop', 'F', '16',
                                     'juillet', '1940', 'Anotherstreet', '7842', 'Thatcity', '010377355',
                                     '0470698621', [0], 1)
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
        page.login_successful("janine_kou@gmail.com", "azertyuiop")

        return True

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
        page = page.set_global_field('Janine', 'cougnou', 'janine_kou@gmail.com', 'azertyuiop', 'F', '16',
                                     'juillet', '1940', 'Anotherstreet', '7842', 'Thatcity', '010377355',
                                     '0470698621', [0], 1)
        time.sleep(2)
        page = page.click_on_submit()
        # registration done

        time.sleep(2)

        return True

    @staticmethod
    def create_job_action(selenium, live_server_url):
        """
        Create a new help demand
        :param selenium:
        :param live_server_url:
        :return: True if the action was successfull,
                 False if the action is impossible now but perhaps could be performed in the future
                 None if the action failed unexcpectedly
        """
        time.sleep(2)
        page = MyCare4Care(selenium)

        time.sleep(3)
        page = page.click_on_i_need_help()  # CreateJobPage
        time.sleep(2)

        # Test create job
        page = page.create_job("I need help", "I need help for bringing me to the shop", "From my place to the shop", 0,
                               "10:30", "01:00", "10", 0, 1, "", "", "", [2, 5], [], [0], True)
        # page.post
        page = page.click_on_post_req()  # We come back to MyCare4Care
        time.sleep(2)

        return True

    @staticmethod
    def accept_participation_action(selenium, live_server_url):
        """
        Accept the help of a user
        :param selenium: The instance of selenium
        :param live_server_url:
        :return: True if the action was successfull,
                 False if the action is impossible now but perhaps could be performed in the future
                 None if the action failed unexcpectedly
        """

        page = MyCare4Care(selenium)
        page = page.click_home()
        time.sleep(1)
        page = HomePage(selenium)

        page = page.click_on_last_offer()  # JobDetailsPage
        time.sleep(1)

        page = page.click_on_choose_member(0)
        time.sleep(1)

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