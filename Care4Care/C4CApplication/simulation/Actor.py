import abc
import random


class Actor(object):
    """
    This class represents an actor in the simulation
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_action_list(self):
        """
        :return: the list of sequences of methods to execute.
        """
        return

    @abc.abstractmethod
    def remove_action_from_action_list(self, action):
        """
        Removes the sequence of action from the action list of the actor
        :param action: The action to remove from the action list
        """
        return

    def act(self, selenium, live_server_url):
        """
        :param selenium: the instance of selenium
        :param live_server_url:
        :return: True if an action was performed,
                 False if there was a problem,
                 None if there is no more actions to run
        """

        action_list = self.get_action_list()
        if len(action_list) == 0:
            return None

        actions_to_perform = action_list[0]  # We take an action randomly

        # We executes all the actions
        result_list = []
        for action in actions_to_perform:
            result = action(selenium, live_server_url)
            if result is None:  # There was a problem => we stop the tests and tells to the scheduler to stop
                return False

        # If the sequence of action was correctly performed now, then we delete it from the action list
        #   in order not to execute it twice
        if not False in result_list:
            self.remove_action_from_action_list(actions_to_perform)

        return True