from django.forms.widgets import ChoiceInput, ChoiceFieldRenderer
from django.utils.encoding import force_text
from django.utils.html import format_html
from C4CApplication.meta.visitor import Visitor
from C4CApplication.meta.non_member import NonMember
from C4CApplication.meta.member import Member
from C4CApplication.meta.volunteer_member import VolunteerMember
from C4CApplication.meta.verified_member import VerifiedMember
from C4CApplication.meta.volunteer_verified import VolunteerVerified
from C4CApplication.meta.branch_officer import BranchOfficer
from C4CApplication.meta.bp_administrator import BPAdministrator
from C4CApplication import models

class UnlabelledChoiceInput(ChoiceInput):
    input_type = None

    def __init__(self, *args, **kwargs):
        super(UnlabelledChoiceInput, self).__init__(*args, **kwargs)

    def render(self, name=None, value=None, attrs=None, choices=()):
        return format_html(
            '{0} {1}', self.tag(), self.choice_label
        )

class UnlabelledRadioChoiceInput(UnlabelledChoiceInput):
    input_type = 'radio'

    def __init__(self, *args, **kwargs):
        super(UnlabelledRadioChoiceInput, self).__init__(*args, **kwargs)
        self.value = force_text(self.value)

class UnlabelledCheckboxChoiceInput(UnlabelledChoiceInput):
    input_type = 'checkbox'

    def __init__(self, *args, **kwargs):
        super(UnlabelledCheckboxChoiceInput, self).__init__(*args, **kwargs)
        self.value = set(force_text(v) for v in self.value)

    def is_checked(self):
        return self.choice_value in self.value

class UnlabelledRadioFieldRenderer(ChoiceFieldRenderer):
    choice_input_class = UnlabelledRadioChoiceInput

class UnlabelledCheckboxFieldRenderer(ChoiceFieldRenderer):
    choice_input_class = UnlabelledCheckboxChoiceInput


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

        if len(db_member) != 1 : 
            return None 
        db_member = db_member[0]
        if db_member.deleted : 
            return None
        member_tag = db_member.tag
        #if db_member is None:  # If the adress was faked
            #return None

    if member_tag & 32:  # BP Administrator
        user = BPAdministrator(db_member)
    elif member_tag & 16:  # Branch officer
        user = BranchOfficer(db_member)
    elif member_tag & 12:  # Volunteer and Verfied member
        user = VolunteerVerified(db_member)
    elif member_tag & 8:  # Volunteer
        user = VolunteerMember(db_member)
    elif member_tag & 4:  # Verified member
        user = VerifiedMember(db_member)
    elif member_tag & 2:  # Member
        user = Member(db_member)
    elif member_tag & 1:  # NonMember
        user = NonMember(db_member)
    else:  # To avoid to give BP admin rights by default if the member_tag is unknown
        return Visitor()
    
    return user
