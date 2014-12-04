from django.views.generic.base import TemplateView
from C4CApplication.models.member import Member
from django.core.exceptions import PermissionDenied
from C4CApplication.views.utils import create_user


class MyCare4CareView(TemplateView):
    template_name = "C4CApplication/MyCare4Care.html"
    user = None

    def dispatch(self, request, *args, **kwargs):
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403
        self.user = create_user(self.request.session['email'])
        return super(MyCare4CareView, self).dispatch(request, *args, **kwargs)
  
    def get_context_data(self, **kwargs):
        context = super(MyCare4CareView, self).get_context_data(**kwargs)
        member = self.user.db_member
        context['member'] = member
        context['connected'] = 'email' in self.request.session
        context['memberTag'] = member.TAG_REVERSE.get(member.tag)
        context['memberActivity'] = 'Active' if member.status else 'Inactive'
        return context