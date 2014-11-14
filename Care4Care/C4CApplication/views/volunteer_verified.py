from C4CApplication.views import VerifiedMember, VolunteerMember


class VolunteerVerified(VolunteerMember, VerifiedMember):
    """
    This class represents a kind of Users that are Volunteer and Verified Members
    """

    def see_job_details(self, job_id):
        #TODO

    def get_job_list(self, show_offers):
        #TODO

    def accept_job(self, job_id, helped_one_email):
        #TODO