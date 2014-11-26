from django.views.generic.edit import FormView
from C4CApplication.views.FeedsMixingView import FeedsMixingView
from C4CApplication.views.forms.LoginForm import LoginForm

# Rq : heritage multiple ; comme FeedsMixingView est la premiere citee, c'est son get_context_data qui sera appele
class HomePageView(FeedsMixingView,FormView):
    template_name = "C4CApplication/HomePage.html"
    form_class = LoginForm
    success_url = "myc4c/"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['loginForm'] = LoginForm(auto_id=False)
        return context

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        self.request.session['email'] = email
        return super(HomePageView, self).form_valid(form)

    def demand_job_list(self):
        member = None # get_member TODO
        return member.get_visible_jobs_list(True)
        
    def offert_job_list(self):
        member = None # get_member TODO
        return member.get_visible_jobs_list(False)
    
    def click_on_job(self, job_number, job_creator_mail):
        member = None # get_member TODO
        # unserailize member
        
        job = member.see_job_details(job_number, job_creator_mail)
        
        # redirect to job page