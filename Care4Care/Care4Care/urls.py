from django.conf.urls import patterns, include, url
from django.contrib import admin
from C4CApplication.views.CreateJobView import CreateJobView
from C4CApplication.views.DonateTimeView import DonateTimeView

from C4CApplication.views.HomePageView import HomePageView
from C4CApplication.views.LogoutView import LogoutView
from C4CApplication.views.MyCare4CareView import MyCare4CareView
from C4CApplication.views.BranchListView import BranchListView
from C4CApplication.views.JobDetailsView import JobDetailsView
from C4CApplication.views.MemberListView import MemberListView
from C4CApplication.views.ConfirmJobDoneView import ConfirmJobDoneView
from C4CApplication.views.ParticipateJobRedirectView import ParticipateJobRedirectView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Care4Care.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home$', HomePageView.as_view(), name='home'),
    url(r'^myc4c/$', MyCare4CareView.as_view(), name='myc4c'),

    url(r'^branchlist$', BranchListView.as_view(), name='branchlist'),
    url(r'^memberlist/(?P<pk>\w+)/$', MemberListView.as_view(), name='memberlist'),

    url(r'^logout$', LogoutView.as_view()),
    url(r'^jobdetails/(?P<pk>\d+)$', JobDetailsView.as_view()),
    url(r'^participatejob/(?P<pk>\d+)$', ParticipateJobRedirectView.as_view(), name='participatejob'),
    #url(r'^confirmjobdone/(?P<pk>\d+)$', ConfirmJobDoneView.as_view()),
    url(r'^profile$', 'C4CApplication.views.test.profile'),

    url(r'^newjob/$', CreateJobView.as_view()),
    url(r'^donate/$', DonateTimeView.as_view())
)
