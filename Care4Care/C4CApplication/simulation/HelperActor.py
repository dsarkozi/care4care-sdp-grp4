from C4CApplication.simulation.Actor import Actor


class HelperActor(Actor):
    """
    This class represents a branch officer that will do some actions
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