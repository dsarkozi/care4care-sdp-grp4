from C4CApplication.views import Member


class VolunteerMember(Member):
    """
    This class represents a kind of Users called Volunteer Members
    """

    def is_job_visible(self, job, db_member):
        """
        :param job:
        :param db_member:
        :return: True if the job created by the member is visible
        """

        #This line have to change if we add the personal network
        return job.visibility == Job.JOB_VISIBILITY['anyone']\
               or job.visibility == Job.JOB_VISIBILITY['volunteer']\
               or (job.visibility == Job.JOB_VISIBILITY['favorites']
                   and db_member.is_favorite(self.db_member))
               
    """def see_job_details(self, job_id, helped_one_email):
        #TODO

    def get_job_list(self, show_offers):
        #TODO

    def accept_job(self, job_id, helped_one_email):
        #TODO"""