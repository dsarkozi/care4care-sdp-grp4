from django.views.decorators.cache import never_cache
from django.views.generic.base import RedirectView
from C4CApplication.models.member import Member
from C4CApplication.views.utils import create_user
from C4CApplication.meta.user import User
from django.core.exceptions import PermissionDenied


class RemoveFavoriteRedirectView(RedirectView):

    
    url = "/favorites"
    user= None
    
    def dispatch(self, request, *args, **kwargs):
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403
        self.user = create_user(self.request.session['email'])
        return super(RemoveFavoriteRedirectView, self).dispatch(request, *args, **kwargs)

    @never_cache
    def get(self, request, *args, **kwargs):
        favorite_mail = kwargs['pk']
        self.user.remove_favorite(favorite_mail)
        return super(RemoveFavoriteRedirectView, self).get(request, *args, **kwargs)