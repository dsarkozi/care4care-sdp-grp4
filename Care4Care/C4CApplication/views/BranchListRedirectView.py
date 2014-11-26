from django.views.decorators.cache import never_cache
from django.views.generic.base import RedirectView
from C4CApplication.models.member import Member
from C4CApplication.views.utils import create_user
from C4CApplication.meta.user import User
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy


class BranchListRedirectView(RedirectView):

    url = ""
    user = None
    
    def dispatch(self, request, *args, **kwargs):
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403
        self.user = create_user(self.request.session['email'])
        return super(BranchListRedirectView, self).dispatch(request, *args, **kwargs)

    @never_cache
    def get(self, request, *args, **kwargs):
        mail_member = kwargs['mail']
        branch_name = kwargs['branch']
        action = kwargs['action']
        
        self.url = reverse_lazy("memberlist", kwargs={'pk': branch_name})
        if action=='0' :  #Remove the member from the branch
            self.user.delete_member_from_branch(branch_name, mail_member)
        elif action=='1' :    #Promote/de-promote to verified
            self.user.modify_tag_member(mail_member, 4)
        else : 
            self.user.modify_tag_member(mail_member, 8)
            
        return super(BranchListRedirectView, self).get(request, *args, **kwargs)