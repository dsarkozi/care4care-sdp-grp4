from C4CApplication.views import Member


class VerifiedMember(Member):
    """
    This class represents a kind of Users called Verified Members
    """

    def see_job_details(self, job_id, helped_one_email):
        """
        :param job_id: id of the job to return
        :param helped_one_email: the email of the 'owner' of the job
        :return: the instance of Job object represented by the 'job_id' if the user can see it
                        otherwise, it returns None
        """
        # TODO a finir
        job_list = Job.objects.filter(number=job_id, mail=helped_one_email)
        if len(job_list) == 0:
            return None

        db_member = (Member.objects.filter(mail=job_list.mail))[0]

        if self.is_job_visible(job_list[0], db_member):
            return job_list[0]
        else:
            return None

    # herited by Non-Member from Member ?
    def get_job_list(self, show_offers):
        """ returns a QuerySet """
        jobs = Job.objects.all(); 
        #TODO a quoi sert show_offers ?
        return jobs

    def accept_job(self, job_id, helped_one_email):
        #TODO
        return False