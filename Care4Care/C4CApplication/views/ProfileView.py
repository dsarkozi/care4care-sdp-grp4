from django.views.generic import DetailView
from django.core.exceptions import PermissionDenied

from C4CApplication.models.member import Member
from C4CApplication.views.utils import create_user


class ProfileView(DetailView):
    template_name = "C4CApplication/Profile.html"
    context_object_name = "member_shown"
    model = Member
    user = None
    
    def get_tag_member(db_member):
        tag = ""
        for v in Member.TAG_CHOICE:
            if v[0] & db_member.tag == v[0]:
                tag += "%s & " % (v[1])
        return tag[:-3]

    def dispatch(self, request, *args, **kwargs):
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403
        self.user = create_user(self.request.session['email'])
        return super(ProfileView, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['member'] = self.user.db_member
        context['tag_member'] = ProfileView.get_tag_member(context['member_shown'])
        context['connected'] = 'email' in self.request.session
        return context

    def get_object(self, queryset=None):
        self.kwargs['pk'] = self.user.db_member.mail
        member_shown = super(ProfileView, self).get_object()
        return member_shown
