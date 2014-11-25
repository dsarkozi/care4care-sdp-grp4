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
        user = create_user(self.request.session['email'], self.request.session['tag'])

        return super(BranchDetailView, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        branch = super(BranchDetailView, self).get_object(queryset=queryset)

        #member_list = user.filter_visible_members(branch.member_set.all())