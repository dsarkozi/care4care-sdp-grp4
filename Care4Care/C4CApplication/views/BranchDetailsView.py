from django.views.generic import DetailView
from django.core.exceptions import PermissionDenied

from C4CApplication.meta import User
from C4CApplication.models import Branch
from C4CApplication.views.utils import create_user


class BranchDetailView(DetailView):
    template_name = "C4CApplication/memberList.html"
    context_object_name = 'branch'
    model = Branch
    user = None

    member_list = None

    def dispatch(self, request, *args, **kwargs):
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403

        # Create the object representing the user
        user = create_user(self.request.session['email'])

        return super(BranchDetailView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BranchDetailView, self).get_context_data()
        # Get the list of the visible members of a branch
        self.member_list = self.user.get_visible_members(self.get_object(self.queryset))
        context['member_list'] = self.member_list