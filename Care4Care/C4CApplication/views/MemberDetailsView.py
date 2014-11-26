from django.views.generic import DetailView
from django.core.exceptions import PermissionDenied
from C4CApplication.views.utils import create_user
from C4CApplication.models.member import Member


class MemberDetailsView(DetailView):
    
    model = Member
    context_object_name = "member"
    template_name = "C4CApplication/memberDetails.html"
    connected_member = None
    
    def dispatch(self, request, *args, **kwargs):
        # Create the object representing the user
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403
        self.connected_member = create_user(self.request.session['email'])

        return super(MemberDetailsView, self).dispatch(request, *args, **kwargs)
    
    
    def get_context_data(self, **kwargs):
        context = {}
        context = super(MemberDetailsView, self).get_context_data(**context)
        context['connected_member'] = self.connected_member.db_member
        return context

    def get_object(self):
        
        member = super(MemberDetailsView, self).get_object()
    
        return member