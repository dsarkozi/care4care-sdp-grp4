from django.views.generic import DetailView
from django.core.exceptions import PermissionDenied
from C4CApplication.views.utils import create_user
from C4CApplication.models.member import Member


class MemberDetailsView(DetailView):
    
    model = Member
    context_object_name = "member_shown"
    template_name = "C4CApplication/memberDetails.html"
    member_shown = None
    
    TAG_REVERSE = {
        1         : 'Non member',               #000001
        2         : 'Member',                   #000010
        4         : 'Verified',                 #000100
        8         : 'Volunteer',                #001000
        16        : 'Branch officer',           #010000
        32        : 'BP admin',                 #100000
    }
    
    def dispatch(self, request, *args, **kwargs):
        # Create the object representing the user
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403
        self.member = create_user(self.request.session['email'])

        return super(MemberDetailsView, self).dispatch(request, *args, **kwargs)
    
    def get_tag_member(db_member):
        tag = ""
        for key, value in MemberDetailsView.TAG_REVERSE.items():
            if key & db_member.tag == key:
                tag += "%s & " % (value)
        return tag[:-3]
    
    
    def get_context_data(self, **kwargs):
        context = {}
        context = super(MemberDetailsView, self).get_context_data(**context)
        context['member'] = self.member.db_member
        context['tag_member'] = MemberDetailsView.get_tag_member(context['member_shown'])
        context['connected'] = 'email' in self.request.session
        context['is_branch_officer'] = self.member.is_branch_officer(context['member_shown'])
        return context

    def get_object(self):
        
        member_shown = super(MemberDetailsView, self).get_object()
    
        return member_shown