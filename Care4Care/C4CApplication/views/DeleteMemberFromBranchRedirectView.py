from django.views.decorators.cache import never_cache
from django.views.generic.base import RedirectView
from C4CApplication.models.member import Member
from C4CApplication.views.utils import create_user
from C4CApplication.meta.user import User
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy


class DeleteMemberFromBranchRedirectView(RedirectView):

    url = ""
    user = None
    
    def dispatch(self, request, *args, **kwargs):
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403
        self.user = create_user(self.request.session['email'])
        return super(DeleteMemberFromBranchRedirectView, self).dispatch(request, *args, **kwargs)

    @never_cache
    def get(self, request, *args, **kwargs):
        mail_member = kwargs['mail']
        branch_name = kwargs['branch']
        self.url = reverse_lazy("memberlist", kwargs={'pk': branch_name})
        self.user.delete_member_from_branch(branch_name, mail_member)
        return super(DeleteMemberFromBranchRedirectView, self).get(request, *args, **kwargs)