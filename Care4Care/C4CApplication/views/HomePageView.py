from django.views.generic.edit import FormView
from C4CApplication.views.FeedsMixingView import FeedsMixingView
from C4CApplication.views.forms.LoginForm import LoginForm
from C4CApplication.models.member import Member
from C4CApplication.models.branch import Branch

from C4CApplication import models
from django.core.urlresolvers import reverse_lazy
from C4CApplication.meta.user import User
from C4CApplication.views.utils import create_user


class HomePageView(FeedsMixingView, FormView):
    template_name = "C4CApplication/HomePage.html"
    form_class = LoginForm
    user = None
    
    def get_success_url(self):
        self.user = create_user(self.request.session['email'])
        return reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        if 'email' in self.request.session:
            context['connected'] = True
            member = Member.objects.get(mail=self.request.session['email'])
            context['member'] = member
        else:
            context['connected'] = False
            brs = Branch.objects.all()
            branches = []
            for i in range(2):
                if brs[i] :
                    branches.append(brs[i])
            context['branches']=branches
        context['loginForm'] = LoginForm(auto_id=False)
        return context

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        
        member = models.Member.objects.filter(mail=email)

        if len(member) == 0 or member[0].deleted:  # if member not found
            return super(HomePageView, self).form_invalid(form)
        member = member[0]  # get the member
        if member.password != password:  # if wrong password
            return super(HomePageView, self).form_invalid(form)
        
        self.request.session['email'] = email
        return super(HomePageView, self).form_valid(form)