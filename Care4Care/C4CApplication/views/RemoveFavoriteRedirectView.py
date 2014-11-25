from django.views.decorators.cache import never_cache
from django.views.generic.base import RedirectView
from C4CApplication.models.member import Member


class RemoveFavoriteRedirectView(RedirectView):

    favorite = None
    
    url = "/favorites"

    @never_cache
    def get(self, request, *args, **kwargs):
        #member = Member.objects.filter(mail=request.session['email'])
        favorite_mail = kwargs['pk']
        self.favorite = Member.objects.filter(mail=favorite_mail)
        #member.remove_favorite(favorite)
        return super(RemoveFavoriteRedirectView, self).get(request, *args, **kwargs)