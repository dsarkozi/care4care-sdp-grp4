from django.views.decorators.cache import never_cache
from django.views.generic.base import RedirectView
from C4CApplication.views.utils import create_user
from C4CApplication.models.member import Member
from django.core.exceptions import PermissionDenied
from django.core.files.storage import FileSystemStorage
from django.core.urlresolvers import reverse_lazy


class DeleteStorage(FileSystemStorage):
    def delete_image(self, name):
        if self.exists(name):
            self.delete(name)
            return True
        else:
            return False


class ModifProfileRedirectView(RedirectView):
    
    url = ""
    
    user = None

    def dispatch(self, request, *args, **kwargs):
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403
        self.user = create_user(self.request.session['email'])
        return super(ModifProfileRedirectView, self).dispatch(request, *args, **kwargs)

    @never_cache
    def get(self, request, *args, **kwargs):
        
        action = kwargs['action']
        
        if action == '0':  # Delete image
            self.url= reverse_lazy("modifprofile")
            image_name = "images/images_profile/%s" % self.user.db_member.mail
            image_name = image_name.replace('@', '.').replace('.', '')+".jpg"
            DeleteStorage().delete_image(image_name)
            self.user.db_member.picture = None
            self.user.db_member.save()
        elif action == '1':  # Delete member
            if not self.user.delete():
                self.url = reverse_lazy("modifprofile")
                return super(ModifProfileRedirectView, self).get(request, *args, **kwargs)
            if 'email' in request.session:
                del request.session['email']

            self.url = reverse_lazy("home")
        else:
            self.url = reverse_lazy("home")
        
        return super(ModifProfileRedirectView, self).get(request, *args, **kwargs)