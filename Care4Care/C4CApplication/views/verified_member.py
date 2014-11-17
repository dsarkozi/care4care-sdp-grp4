from C4CApplication.views import Member


class VerifiedMember(Member):
    """
    This class represents a kind of Users called Verified Members
    """

    # serieux c'est sense faire/renvoyer quoi ? 
    def see_job_details(self, job_id):
        #TODO
        return False

    def get_job_list(self, show_offers):
        """ returns a QuerySet """
        jobs = Job.objects.all(); 
        #TODO a quoi sert show_offers ?
        return jobs

    def accept_job(self, job_id, helped_one_email):
        #TODO
        return False