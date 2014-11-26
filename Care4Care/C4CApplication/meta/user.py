import abc

from time import strftime, gmtime


class User(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def is_job_visible(self, job, db_member):
        """
        :param job:
        :param db_member:
        :return: True if the job created by the member is visible
        """

    @abc.abstractmethod
    def see_job_details(self, job_number, job_creator_mail):
        """
        :param job_number: id of the job to return
        :param job_creator_mail: the email of the 'owner' of the job
        :return: the instance of Job object represented by the 'job_number' if the user can see it
                        otherwise, it returns None
        """
        return

    @abc.abstractmethod
    def get_visible_job_list(self, show_offers):
        """
        :param show_offers: the type of the list of the jobs to return
        :return: the list of Job objects visible by the user
            (offers if 'show_offers' is true and otherwise the demands)
        """
        return

    @abc.abstractmethod
    def get_involved_job_list(self, show_offers):
        """
        :param show_offers: the type of the list of the jobs to return
        :return: the list of Job objects in which the user is involved
            (offers if 'show_offers' is true and otherwise the demands)
        """
        return


    @abc.abstractmethod
    def accept_job(self, job_number, job_creator_mail):
        """
        Puts the member on the list of possible helpers for a pending job.
        The helped one will be warned by email (this email is the parameter 'job_creator_mail').

        :param job_number: the if of the job to accept
        :param job_creator_mail: the email of the 'owner' of the job
        :return: False if there was a problem and True otherwise
        """
        return
    
    @abc.abstractmethod
    def stop_participate_job(self, job_number, job_creator_mail):
        """
        Remove the member on the list of possible helpers for a pending job.

        :param job_number: the if of the job to accept
        :param job_creator_mail: the email of the 'owner' of the job
        :return: False if there was a problem and True otherwise
        """
        return

    @abc.abstractmethod
    def register_job_done(self, job_number, job_creator_mail, helped_one_email=None, new_time=0):
        """
        Registers a job as done (with the new time to put).
        The helped one will be warned by email and will be able to accept the 'payment' or not

        :param job_number: it's the number of the job created by the job_creator_mail
        :param job_creator_mail: The mail of the creator of the job
        :param helped_one_email: it can't be None
        :param new_time:
        :return: False if there was a problem and True otherwise.
        """
        return

    @abc.abstractmethod
    def accept_help(self, job_number, job_creator_mail, helper_email):
        """
        Chooses the member (with email stored in 'helper_email') to do the job (with id stored in 'number')
        The chosen helper is warned by email

        :param job_number: it's the number of the job created by the job_creator_mail
        :param job_creator_mail: The mail of the creator of the job
        :param helper_email:
        :return: False if there was a problem and True otherwise
        """
        return

    @abc.abstractmethod
    def create_job(self, branch_name, date=strftime('%Y-%m-%d', gmtime()), is_demand=False, comment=None,
                   start_time=0, frequency=0, km=0, time=0, category=1, address=None, visibility='volunteer'):
        """
        Creates a help offer (the parameters will be used to fill the database).

        :param branch_name: The branch to which belongs the job
        :param date: The date of the job
        :param is_demand: True if it's a demand, false otherwise
        :param comment: Comment of the job
        :param start_time: The hour of the beginning of the job in minute. Example : 14h30 -> 14*60+30 = 870
        :param frequency: The frequency of the job. (0=Once, 1=daily, 2=weekly, ...)
        :param km: The number of km to do the job
        :param time: The time to do the job
        :param category: The category of the job. (1=shopping, 2=visit, 3=transport)
        :param address: The address where the job will be done
        :param visibility: Which people can see the job.
        :return: False if there was a problem and True otherwise.
        """
        return
    
    @abc.abstractmethod
    def delete_job(self, job_number):
        """
        Delete the number eme job of the user

        :param job_number: The number of the job of the user to delete.
        """
        return

    @abc.abstractmethod
    def accept_bill(self, job_number, job_creator_mail, amount):
        """
        Accepts the bill and transfers money to the helper

        :param job_number: it's the number of the job created by the job_creator_mail
        :param job_creator_mail: The mail of the creator of the job
        :param helper_email:
        :param amount: amount of the bill
        :return: False if there was a problem and True otherwise.
        """
        return

    @abc.abstractmethod
    def refuse_bill(self, job_number, job_creator_mail, helper_email):
        """
        Refuses the bill and warns the branch officer by email

        :param job_number: it's the number of the job created by the job_creator_mail
        :param job_creator_mail: The mail of the creator of the job
        :param helper_email:
        :return: False if there was a problem and True otherwise.
        """
        return

    @abc.abstractmethod
    def transfer_time(self, destination_email, time):
        """
        Transfers 'time' to a member with 'destination_email' as email

        :param destination_email: the email address of the member to transfer time
        :return: False if there was a problem and True otherwise.
        """
        return

    @abc.abstractmethod
    def make_donation(self, time, branch_name=None):
        """
        Makes a donation to the branch of the member

        :param branch_name:
        :param time:
        :return:
        """
        return

    @abc.abstractmethod
    def delete_member_from_branch(self, branch_name, deleted_one_email):
        """
        Delete the member from the branch

        :param branch_name: The name of the branch that the branch_officer belongs to
        :param deleted_one_email: The mail of the member the branch_officer want to remove from
                                    the branch.
        :return: False if there was a problem and True otherwise.
        """
        return

    @abc.abstractmethod
    def delete_member_from_site(self, deleted_one_email):
        """
        Put the status of the member as deleted (TODO add a deleted field to member ?)
        :param deleted_one_email: the email of the person to delete
        :return: False if there was a problem and True otherwise.
        """
        return

    @abc.abstractmethod
    def log_as_member(self, email, session):
        """
        Logs the current user as the one specified by the email (by modifying the session variables)
        :param email: the email of the member to log in as
        :param session: the dictionary containing the session variables
        :return: False if there was a problem and True otherwise.
        """
        return

    @abc.abstractmethod
    def give_branch_control(self, branch_name, new_branch_officer_email):
        """
        Set the control of a branch to an another branch_officer, which is represented by his mail
        :param branch_name: the name of the branch that will change of the branch_officer
        :param new_branch_officer_email: the new branch_officer that will control the branch
        :return: False if there was a problem and True otherwise.
        """
        return

    @abc.abstractmethod
    def modify_tag_member(self, email, new_tag):
        """
        Modify the tag of the member represented by the email,
        and set his tag to the new_tag
        :param email: mail of the member we need to modify the tag
        :param new_tag: new tag to assign to the member
        :return: False if there was a problem and True otherwise.
        """
        return

    @abc.abstractmethod
    def transfer_money_from_branch(self, time, branch_name, destination_email):
        """
        Make a gift by taking some time from the branch to the member represented
        by the destinaion_mail.
        :param time: the amount of time that we give as a gift
        :param branch_name: the branch that give the donation
        :param destination_email: the member that receive the donation
        :return: False if there was a problem and True otherwise.
        """
        return

    @abc.abstractmethod
    def create_branch(self, name, town, branch_officer_email=None, address=None):
        """
        Create a new branch with the parameter
        :param name: name of the new branch
        :param town: town of the new branch
        :param branch_officer_email: mail of the branch_officer that will manage the branch
        :param address: address of the branch, for meeting, or other
        :return: False if there was a problem and True otherwise.
        """
        return

    @abc.abstractmethod
    def remove_branch(self, branch_name):
        """
        Remove a branch from the application
        :param branch_name: the name of the branch to remove
        :return: False if there was a problem and True otherwise.
        """
        return

    @abc.abstractmethod
    def transfer_bp_admin_rights(self, new_bp_admin_email):
        """
        The bp admin abandon his rights, and give them to someone else.
        :param new_bp_admin_email:
        :return: False if there was a problem and True otherwise.
        """
        return
    
    @abc.abstractmethod
    def add_favorite(self, favorite_mail):
        """
        Add a favorite to self
        :param favorite_mail : the mail of the favorite
        :return : false if the member is not added to favorites (because it doesn't exist for example)
        """
        return
    
    @abc.abstractmethod
    def remove_favorite(self, favorite_mail):
        """
        Remove a favorite to self
        :param favorite_mail : the mail of the favorite
        :return : false if the member is not removed from favorites (because it doesn't exist for example)
        """
        return

    @abc.abstractmethod
    def is_member_visible(self, member):
        """
        :param member:
        :return: True if the member is visible for the current user and False otherwise
        """
        return

    @abc.abstractmethod
    def get_visible_members(self, branch):
        """
        :param branch: if it is not None, it gets only the members that are in a specific branch
        :return: the list of the visible members (of the branch specified if the parameter is not set to None)
        """
        return
    
    @abc.abstractmethod
    def change_status(self, active):
        """
        :param active
        :return: True
        """
        return
