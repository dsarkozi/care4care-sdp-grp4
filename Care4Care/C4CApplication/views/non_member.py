from C4CApplication.views import User


class NonMember(User):
    """
    This class represents a kind of Users called Non Members
    """

    def __init__(self, db_member):
        self.db_member = db_member

    def see_job_details(self, job_id):
        """
        :param job_id:
        :return: the instance of Job object represented by the 'job_id' if the user can see it
                        otherwise, it returns None
        """

    def get_job_list(self, show_offers):
        """
        :param show_offers:
        :return: the list of Job objects visible by the user
            (offers if 'show_offers' is true and otherwise the demands)
        """

    def accept_job(self, job_id, helped_one_email):
        """
        Puts the member on the list of possible helpers for a pending job.
        The helped one will be warned by email (this email is the parameter 'helped_one_email').

        :param job_id:
        :param helped_one_email:
        :return: False if there was a problem and True otherwise
        """

    def create_job(self, start_time, time, comment=None, frequency=0, km=0,
                   category=1, address=None, visibility='anyone'):
        """
        Creates a help offer (the parameters will be used to fill the database).

        :param start_time:
        :param time:
        :param comment:
        :param frequency:
        :param km:
        :param category:
        :param address:
        :param visibility:
        :return: False if there was a problem and True otherwise.
        """

    def register_job_done(self, job_id):
        """
        Registers a job as done (with no time because a Non Member cannot 'earn' time)

        :param job_id:
        :return: False if there was a problem and True otherwise.
        """

