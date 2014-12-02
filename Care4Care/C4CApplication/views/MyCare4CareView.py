from django.views.generic.base import TemplateView
from C4CApplication.models.member import Member
from django.core.exceptions import PermissionDenied


class MyCare4CareView(TemplateView):
    template_name = "C4CApplication/MyCare4Care.html"

    def get_context_data(self, **kwargs):
        
        if 'email' not in self.request.session:
            raise PermissionDenied  # HTTP 403
        context = super(MyCare4CareView, self).get_context_data(**kwargs)
        member = Member.objects.get(mail=self.request.session['email'])
        context['member'] = member
        context['memberTag'] = member.TAG_REVERSE.get(member.tag)
        context['memberActivity'] = 'Active' if member.status else 'Inactive'
        return context