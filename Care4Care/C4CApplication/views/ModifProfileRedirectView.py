from django.views.decorators.cache import never_cache
from django.views.generic.base import RedirectView
from C4CApplication.views.utils import create_user
from C4CApplication.models.member import Member
from django.core.exceptions import PermissionDenied


class ModifProfileRedirectView(RedirectView):
    
    url = ""
    
    connected_member = None

    def dispatch(self, request, *args, **kwargs):
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403
        self.connected_member = create_user(self.request.session['email'])
        return super(ModifProfileRedirectView, self).dispatch(request, *args, **kwargs)

    @never_cache
    def get(self, request, *args, **kwargs):
        
        action = kwargs['action']
        
        if action=='0': #Delete image
            self.url="/modifprofile/"
        elif acction=='1':  #Delete member
            self.url="/"
        else :  #Sinon
            self.url="/"
        
        return super(ModifProfileRedirectView, self).get(request, *args, **kwargs)