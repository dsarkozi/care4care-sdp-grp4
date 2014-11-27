from C4CApplication.meta import Member
from C4CApplication.models import Job
from C4CApplication import models


class VerifiedMember(Member):
    """
    This class represents a kind of Users called Verified Members
    """

    def is_job_visible(self, job, db_member):
        """
        :param job:
        :param db_member:
        :return: True if the job created by the verified member is visible
        """

        #This line have to change if we add the personal network
        return (job.visibility & Job.JOB_VISIBILITY['anyone']) == 1\
               or (job.visibility & Job.JOB_VISIBILITY['verified']) == 1\
               or (job.visibility & Job.JOB_VISIBILITY['favorites'] == 1
                   and db_member.is_favorite(self.db_member))\
               or db_member == self.db_member

    def see_job_details(self, job_number, job_creator_mail):
        """
        :param job_number: id of the job to return
        :param job_creator_mail: the email of the 'owner' of the job
        :return: the instance of Job object represented by the 'job_number' if the user can see it
                        otherwise, it returns None
        """
        return self.see_job_details_base(job_number, job_creator_mail, self.is_job_visible)

    def get_job_list(self, show_offers):
        """
        :param show_offers: the type of the list of the jobs to return
        :return: the list of Job objects visible by the user
            (offers if 'show_offers' is true and otherwise the demands)
        """
        return self.get_visible_job_list_base(show_offers, self.is_job_visible)

    def accept_job(self, job_number, job_creator_mail):
        """
        Puts the member on the list of possible helpers for a pending job.
        The helped one will be warned by email (this email is the parameter 'job_creator_mail').

        :param job_number: the if of the job to accept
        :param job_creator_mail: the email of the 'owner' of the job
        :return: False if there was a problem and True otherwise
        """
        return self.accept_job_base(job_number, job_creator_mail, self.is_job_visible)

    def is_member_visible(self, member):
        if member.deleted : return False
        
        #this line must be modified if we add the personal network
        return member.visibility & models.Member.MEMBER_VISIBILITY['anyone']\
               or member.visibility & models.Member.MEMBER_VISIBILITY['verified']\
               or (member.visibility & models.Member.MEMBER_VISIBILITY['favorites']
                   and member.is_favorite(self.db_member))\
               or member == self.db_member

    def get_visible_members(self, branch):
        return self.get_visible_members_base(self.is_member_visible, branch)