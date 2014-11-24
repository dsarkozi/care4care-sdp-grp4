from django.conf.urls import patterns, include, url
from django.contrib import admin
from C4CApplication.views.CreateJob1View import CreateJob1View

from C4CApplication.views.HomePageView import HomePageView
from C4CApplication.views.LogoutView import LogoutView
from C4CApplication.views.MyCare4CareView import MyCare4CareView
from C4CApplication.views.BranchListView import BranchListView
from C4CApplication.views.JobDetailsView import JobDetailsView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Care4Care.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home$', HomePageView.as_view(), name='home'),

    url(r'^myc4c/$', MyCare4CareView.as_view(), name='myc4c'),
    url(r'^branchlist$', BranchListView.as_view(), name='branchlist'),
    url(r'^logout$', LogoutView.as_view()),
    url(r'^jobdetails/(?P<pk>\d+)$',JobDetailsView.as_view()), 
    url(r'^confirmjobdone/(?P<pk>\d+)$', ...),

    url(r'^newjob1/', CreateJob1View.as_view()),
)
