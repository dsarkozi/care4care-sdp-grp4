from django.views.decorators.cache import never_cache
from django.views.generic.base import RedirectView
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy

from C4CApplication.views.utils import create_user


class RemoveFavoriteRedirectView(RedirectView):

    
    url = reverse_lazy("favorites")
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