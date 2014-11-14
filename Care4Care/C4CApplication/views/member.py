from C4CApplication.views import NonMember


class Member(NonMember):
    """
    This class represents a kind of Users called Members
    """

    def accept_help(self, job_id, helper_email):
        """
        Chooses the member (with email stored in 'helper_email') to fo the job (with id stored in 'job_id')
        The chosen helper is warned by email

        :param job_id:
        :param helper_email:
        :return: False if there was a problem and True otherwise
        """

    def create_job(self, is_demand=False, comment=None, start_time=0, frequency=0, km=0,
                   time=0, category=1, address=None, visibility='anyone'):
        """
        Creates a help offer (the parameters will be used to fill the database).

        :param is_demand:
        :param comment:
        :param start_time:
        :param frequency:
        :param km:
        :param time:
        :param category:
        :param address:
        :param visibility:
        :return: False if there was a problem and True otherwise.
        """

    def register_job_done(self, job_id, helped_one_email=None, new_time=0):
        """
        Registers a job as done (with the new time to put).
        The helped one will be warned by email and will be able to accept the 'payment' or not

        :param job_id:
        :param helped_one_email:
        :param new_time:
        :return: False if there was a problem and True otherwise.
        """

    def accept_bill(self, job_id, helper_email):
        """
        Accepts the bill and transfers money to the helper

        :param job_id:
        :param helper_email:
        :return: False if there was a problem and Ture otherwise.
        """

    def refuse_bill(self, job_id, helper_email):
        """
        Refuses the bill and warns the branch officer by email

        :param job_id:
        :param helper_email:
        :return: False if there was a problem and Ture otherwise.
        """

    def transfer_time(self, destination_email, time):
        """
        Transfers 'time' to a member with 'destination_email' as email

        :param destination_email: the email address of the member to transfer time
        :return: False if there was a problem and Ture otherwise.
        """

    def make_donation(self, time, branch_name=None):
        """
        Makes a donation to the branch of the member

        :param branch_name:
        :param time:
        :return:
        """