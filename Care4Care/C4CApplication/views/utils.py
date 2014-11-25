from C4CApplication.meta.visitor import Visitor
from C4CApplication.meta.non_member import NonMember
from C4CApplication.meta.member import Member
from C4CApplication.meta.volunteer_member import VolunteerMember
from C4CApplication.meta.verified_member import VerifiedMember
from C4CApplication.meta.volunteer_verified import VolunteerVerified
from C4CApplication.meta.branch_officer import BranchOfficer
from C4CApplication.meta.bp_administrator import BPAdministrator

from C4CApplication import models


def create_user(member_email):
    """
    :param member_email:
    :return: the object of the class representing the priviledge of the users
    """

    if member_email is None:
        member_tag = 0
        db_member = None
    else:
        db_member = models.Member.objects.filter(mail=member_email)
        member_tag = db_member.tag
        if db_member is None:  # If the adress was faked
            return None

    if member_tag & 32:  # BP Administrator
        user = BPAdministrator(member_email)
    elif member_tag & 16:  # Branch officer
        user = BranchOfficer(member_email)
    elif member_tag & 12:  # Volunteer and Verfied member
        user = VolunteerVerified(member_email)
    elif member_tag & 8:  # Volunteer
        user = VolunteerMember(member_email)
    elif member_tag & 4:  # Verified member
        user = VerifiedMember(member_email)
    elif member_tag & 2:  # Member
        user = Member(member_email)
    elif db_member & 1:  # NonMember
        user = NonMember(member_email)
    else:  # To avoid to give BP admin rights by default if the member_tag is unknown
        return Visitor()