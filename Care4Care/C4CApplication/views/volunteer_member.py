from C4CApplication.views import Member
from C4CApplication.models import Job


class VolunteerMember(Member):
    """
    This class represents a kind of Users called Volunteer Members
    """

    def is_job_visible(self, job, db_member):
        """
        :param job:
        :param db_member:
        :return: True if the job created by the verified member is visible
        """

        #This line have to change if we add the personal network
        return (job.visibility & Job.JOB_VISIBILITY['anyone']) == 1\
               or (job.visibility & Job.JOB_VISIBILITY['volunteer']) == 1\
               or (job.visibility == Job.JOB_VISIBILITY['favorites']
                   and db_member.is_favorite(self.db_member))

    def see_job_details(self, job_id, helped_one_email):
        """
        :param job_id: id of the job to return
        :param helped_one_email: the email of the 'owner' of the job
        :return: the instance of Job object represented by the 'job_id' if the user can see it
                        otherwise, it returns None
        """
        return self.see_job_details_base(job_id, helped_one_email, self.is_job_visible)

    def get_job_list(self, show_offers):
        """
        :param show_offers: the type of the list of the jobs to return
        :return: the list of Job objects visible by the user
            (offers if 'show_offers' is true and otherwise the demands)
        """
        return self.get_job_list_base(show_offers, self.is_job_visible)

    def accept_job(self, job_id, helped_one_email):
        """
        Puts the member on the list of possible helpers for a pending job.
        The helped one will be warned by email (this email is the parameter 'helped_one_email').

        :param job_id: the if of the job to accept
        :param helped_one_email: the email of the 'owner' of the job
        :return: False if there was a problem and True otherwise
        """
        return self.accept_job_base(job_id, helped_one_email, self.is_job_visible)