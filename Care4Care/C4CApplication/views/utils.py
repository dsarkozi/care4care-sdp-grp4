from C4CApplication.meta.visitor import Visitor
from C4CApplication.meta.non_member import NonMember
from C4CApplication.meta.member import Member
from C4CApplication.meta.volunteer_member import VolunteerMember
from C4CApplication.meta.verified_member import VerifiedMember
from C4CApplication.meta.volunteer_verified import VolunteerVerified
from C4CApplication.meta.branch_officer import BranchOfficer
from C4CApplication.meta.bp_administrator import BPAdministrator

@staticmethod
def create_user(member_email, member_tag):
    """
    :param member_email:
    :param member_tag:
    :return: the object of the class representing the priviledge of the users
    """

    if member_tag == 1:  # NonMember
        user = NonMember(member_email)
    elif member_tag == 2:  # Member
        user = Member(member_email)
    elif member_tag == 4:  # Verified member
        user = VerifiedMember(member_email)
    elif member_tag == 8:  # Volunteer
        user = VolunteerMember(member_email)
    elif member_tag == 12:  # Volunteer and Verfied member
        user = VolunteerVerified(member_email)
    elif member_tag == 16:  # Branch officer
        user = BranchOfficer(member_email)
    elif member_tag == 32:  # BP Administrator
        user = BPAdministrator(member_email)
    else:  # To avoid to give BP admin rights by default if the member_tag is unknown
        return Visitor()

    if user.db_member is not None:  # If the adress wasn't faked
        return user
    else:
        return None