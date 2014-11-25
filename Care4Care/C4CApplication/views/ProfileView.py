from django.views.generic import DetailView
from C4CApplication.models.member import Member

class ProfileView(DetailView):
    template_name = "C4CApplication/Profile.html"
    context_object_name = "member"
    model = Member

    def get_object(self):
        member = super(ProfileView, self).get_object()
    
        return member
