from django.views.decorators.cache import never_cache
from django.views.generic.base import RedirectView

from C4CApplication.views.utils import create_user


class MemberDetailsRedirectView(RedirectView):
    
    url = ""
    
    connected_member = None

    def dispatch(self, request, *args, **kwargs):
        # Create the object representing the user
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403
        self.connected_member = create_user(self.request.session['email'])

        return super(MemberDetailsRedirectView, self).dispatch(request, *args, **kwargs)

    @never_cache
    def get(self, request, *args, **kwargs):
        
        member_to_ad_as_a_friend_mail = kwargs['pk']
        self.url = "/memberdetails/"+str(member_to_ad_as_a_friend_mail)
        
        self.connected_member.add_favorite( member_to_ad_as_a_friend_mail)
        
        return super(MemberDetailsRedirectView, self).get(request, *args, **kwargs)