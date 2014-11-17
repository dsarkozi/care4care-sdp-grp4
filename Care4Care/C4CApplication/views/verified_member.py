from C4CApplication.views import Member, Job


class VerifiedMember(Member):
    """
    This class represents a kind of Users called Verified Members
    """

    def is_job_visible(self, job, db_member):
        """
        :param job:
        :param db_member:
        :return: True if the job created by the member is visible
        """

        #This line have to change if we add the personal network
        return job.visibility == Job.JOB_VISIBILITY['anyone']\
               or job.visibility == Job.JOB_VISIBILITY['verified']\
               or (job.visibility == Job.JOB_VISIBILITY['favorites']
                   and db_member.is_favorite(self.db_member))

    def see_job_details(self, job_id, helped_one_email):
        """
        :param job_id: id of the job to return
        :param helped_one_email: the email of the 'owner' of the job
        :return: the instance of Job object represented by the 'job_id' if the user can see it
                        otherwise, it returns None
        """
        job_list = Job.objects.filter(number=job_id, mail=helped_one_email)
        if len(job_list) == 0:
            return None
        job = job_list[0]

        db_member = (Member.objects.filter(mail=job_list.mail))[0]

        if self.is_job_visible(job, db_member):
            return job
        else:
            return None

    # En fait en redéfinissant juste is_visible c'est bon, nan ? (idem pour see_job_details
    """def get_job_list(self, show_offers):
        """ """returns a QuerySet """ """
        jobs = Job.objects.all()
        #TODO a quoi sert show_offers ?
        return jobs"""

    def accept_job(self, job_id, helped_one_email):
        #TODO
        return False