from django.views.generic.base import TemplateView
from C4CApplication.models.member import Member


class MyCare4CareView(TemplateView):
    template_name = "C4CApplication/MyCare4Care.html"

    def get_context_data(self, **kwargs):
        context = super(MyCare4CareView, self).get_context_data(**kwargs)
        member = Member.objects.get(mail=self.request.session['email'])
        context['member'] = member
        context['memberTag'] = member.TAG.get(member.tag)
        context['memberActivity'] = 'Active' if member.status else 'Inactive'
        return context