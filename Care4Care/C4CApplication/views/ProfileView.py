from django.views.generic import DetailView
from C4CApplication.models.member import Member
from django.core.exceptions import PermissionDenied
from C4CApplication.views.utils import create_user

class ProfileView(DetailView):
    template_name = "C4CApplication/Profile.html"
    context_object_name = "member_shown"
    model = Member

    def dispatch(self, request, *args, **kwargs):
       if 'email' not in self.request.session:
          raise PermissionDenied  # HTTP 403
       self.user = create_user(self.request.session['email'])
       return super(ProfileView, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
       context = super(ProfileView, self).get_context_data(**kwargs)
       context['member'] = self.user.db_member
       return context
  
    def get_object(self):
        member_shown = super(ProfileView, self).get_object()
    
        return member_shown
