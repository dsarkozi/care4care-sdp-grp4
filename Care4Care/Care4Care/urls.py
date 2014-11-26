from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import ListView

from C4CApplication.views.CreateJobView import CreateJobView
from C4CApplication.views.DonateTimeView import DonateTimeView

from C4CApplication.views.HomePageView import HomePageView
from C4CApplication.views.LogoutView import LogoutView
from C4CApplication.views.MyCare4CareView import MyCare4CareView
from C4CApplication.views.BranchListView import BranchListView
from C4CApplication.views.JobDetailsView import JobDetailsView
from C4CApplication.views.BranchDetailsView import BranchDetailView
from C4CApplication.views.ConfirmJobDoneView import ConfirmJobDoneView

from C4CApplication.views.ProfileView import ProfileView
from C4CApplication.views.MemberDetailsView import MemberDetailsView
from C4CApplication.views.MemberDetailsRedirectView import MemberDetailsRedirectView

from C4CApplication.views.ParticipateJobRedirectView import ParticipateJobRedirectView
from C4CApplication.views.ListMessages import ListMessages

from C4CApplication.views.viewMessage import ViewMessage

from C4CApplication.views.AcceptBillView import AcceptBillView
from C4CApplication.views.ConfirmBillRedirectView import ConfirmBillRedirectView

from C4CApplication.views.FavoritesView import FavoritesView
from C4CApplication.views.RemoveFavoriteRedirectView import RemoveFavoriteRedirectView

from C4CApplication.views.TransferRightsView import TransferRightsView
from C4CApplication.views.CreateBranchView import CreateBranchView

from C4CApplication.views.ChangeActivityView import ChangeActivityView
from C4CApplication.views.ChangeActivityRedirectView import ChangeActivityRedirectView

from C4CApplication.views.DeleteMemberFromBranchRedirectView import DeleteMemberFromBranchRedirectView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Care4Care.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^myc4c/$', MyCare4CareView.as_view(), name='myc4c'),
    
    url(r'^myc4c/changeActivity$', ChangeActivityView.as_view(), name='changeActivity'),
    url(r'^myc4c/changeActivityRedirect/(?P<active>\w+)$', ChangeActivityRedirectView.as_view(), name='changeActivityRedirect'),

    url(r'^branchlist$', BranchListView.as_view(), name='branchlist'),
    url(r'^memberlist/(?P<pk>\w+)/$', BranchDetailView.as_view(), name='memberlist'),

    url(r'^logout$', LogoutView.as_view()),
    url(r'^jobdetails/(?P<pk>\d+)$', JobDetailsView.as_view()),
    url(r'^participatejob/(?P<pk>\d+)/(?P<mail>(\w+.)+\w+@(\w+.)+\w+)$', ParticipateJobRedirectView.as_view(), name='participatejob'),
    url(r'^confirmjobdone/(?P<pk>\d+)$', ConfirmJobDoneView.as_view(), name='confirmjobdone'),
    
    url(r'^profile$', 'C4CApplication.views.test.profile'),
    url(r'^memberdetails/(?P<pk>(\w+.)+\w+@(\w+.)+\w+)$', MemberDetailsView.as_view(), name='memberdetails'),
    url(r'^memberdetailsredirect/(?P<pk>(\w+.)+\w+@(\w+.)+\w+)/$', MemberDetailsRedirectView.as_view(), name='memberdetailsredirect'),
    url(r'^favorites$', FavoritesView.as_view(), name='favorites'),
    url(r'^removeFavorite/(?P<pk>(\w+.)+\w+@(\w+.)+\w+)/$', RemoveFavoriteRedirectView.as_view(), name='removeFavorite'),
    url(r'^profile/(?P<pk>\d+)$', ProfileView.as_view(), name='profile'),
    url(r'^inscription$', 'C4CApplication.views.inscription.inscription',name='inscription'),
    url(r'^new_message$', 'C4CApplication.views.nouveau_message.nouveau_message', name='newmessage'),

    url(r'^acceptbill/(?P<pk>\d+)$', AcceptBillView.as_view(), name='acceptBill'),
    url(r'^confirmBill/(?P<pk>\d+)/(?P<confirm>\d+)$', ConfirmBillRedirectView.as_view(), name='confirmBill'),

    url(r'^transferrights/$', TransferRightsView.as_view(), name='transferrights'),
    url(r'^createbranch/$', CreateBranchView.as_view(), name='createbranch'),

    url(r'^deletememberfrombranch/(?P<branch>\w+)/(?P<mail>(\w+.)+\w+@(\w+.)+\w+)$', DeleteMemberFromBranchRedirectView.as_view(), name='deletememberfrombranch'),

    url(r'newjob/$', CreateJobView.as_view()),
    url(r'donate/$', DonateTimeView.as_view()),
    
    url(r'^list_messages/(?P<received>\d+)$', ListMessages.as_view(), name='messageList'),
    url(r'^message/(?P<pk>\w+)/$', ViewMessage.as_view(), name='message'),


)
