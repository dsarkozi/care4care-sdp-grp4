import time

from C4CApplication.page_objects.BranchListPage import BranchListPage
from C4CApplication.page_objects.FixedPage import FixedPage
from C4CApplication.simulation.Actor import Actor
from C4CApplication.page_objects.HomePage import HomePage
from C4CApplication.page_objects.MyCare4Care import MyCare4Care


class BranchOfficerActor(Actor):
    """
    This class represents a branch officer that will do some actions
    """

    action_list = None

    def get_action_list(self):

        if self.action_list is None:
            self.action_list = [
                [self.login_action, self.log_as_member, self.create_job, self.logout_action, self.logout_action]
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
        page.login_successful("kim.mens@gmail.com", "azertyuiop")  # Kim is branch officer of LLN
        time.sleep(2)

        return True

    @staticmethod
    def log_as_member(selenium, live_server_url):
        """
        Login as a member of its branch and create an demand for him
        :param selenium: The instance of selenium
        :param live_server_url:
        :return: True if the action was successfull,
                 False if the action is impossible now but perhaps could be performed in the future
                 None if the action failed unexcpectedly
        """

        page = FixedPage(selenium)
        page.click_on_care4care_branches()

        time.sleep(1)
        page = BranchListPage(selenium)
        page = page.click_on_branch_details(0)  # click on lln -> MemberListPage
        time.sleep(1)

        page = page.click_on_member(2)  # click on a member : Armand -> MemberDetailsPage
        time.sleep(1)
        page = page.click_on_log_as_member()  # log as the member
        time.sleep(1)

        return True

    @staticmethod
    def create_job(selenium, live_server_url):
        """
        Create a new job
        :param selenium: The instance of selenium
        :param live_server_url:
        :return: True if the action was successfull,
                 False if the action is impossible now but perhaps could be performed in the future
                 None if the action failed unexcpectedly
        """

        page = MyCare4Care(selenium)
        time.sleep(3)
        page = page.click_on_i_need_help()  # CreateJobPage
        time.sleep(2)

        # Test create job
        page = page.create_job("I need help", "I need help for bringing me to the shop", "From my place to the shop", 0, "10:30", \
                               "01:00", "10", 0, 1, "", "", "", [2, 5], [], [0], True)
        # page.post
        page.click_on_post_req()  # We arrive at MyCare4CarePage
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
        time.sleep(2)
        page = MyCare4Care(selenium)
        page.click_home()
        time.sleep(2)

        # Logout
        page = HomePage(selenium)
        page.click_on_logout()
        time.sleep(2)

        return True