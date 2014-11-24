from django.views.generic.list import ListView
from django.core.exceptions import PermissionDenied

from C4CApplication.meta import User
from C4CApplication.models import Member


class MemberListView(ListView):
    template_name = "C4CApplication/memberList.html"
    model = Member
    queryset = None
    user = None

    def dispatch(self, request, *args, **kwargs):
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403
        return super(MemberListView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        #TODO get back the list from the get_member_list method of the user
        return super(MemberListView, self).get_queryset()