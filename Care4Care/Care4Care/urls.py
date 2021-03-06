from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from C4CApplication.views.SearchJobView import SearchJobView
from C4CApplication.views.AccountStatsView import AccountStatsView
from C4CApplication.views.CreateJobView import CreateJobView
from C4CApplication.views.DonateTimeView import DonateTimeView
from C4CApplication.views.EIDRedirectView import EIDRedirectView
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
from C4CApplication.views.ListMessagesView import ListMessagesView
from C4CApplication.views.MessageView import MessageView
from C4CApplication.views.AcceptBillView import AcceptBillView
from C4CApplication.views.ConfirmBillRedirectView import ConfirmBillRedirectView
from C4CApplication.views.FavoritesView import FavoritesView
from C4CApplication.views.RegistrationView import RegistrationView
from C4CApplication.views.RemoveFavoriteRedirectView import RemoveFavoriteRedirectView
from C4CApplication.views.TransferRightsView import TransferRightsView
from C4CApplication.views.TransferRightsBranchView import TransferRightsBranchView
from C4CApplication.views.DeleteMemberBPAView import DeleteMemberBPAView
from C4CApplication.views.ChangeActivityView import ChangeActivityView
from C4CApplication.views.ChangeActivityRedirectView import ChangeActivityRedirectView
from C4CApplication.views.BranchListRedirectView import BranchListRedirectView
from C4CApplication.views.LoginAsMemberRedirectView import LoginAsMemberRedirectView
from C4CApplication.views.ModifProfileView import ModifProfileView
from C4CApplication.views.ModifProfileRedirectView import ModifProfileRedirectView
from C4CApplication.views.NewMessageView import NewMessageView
from C4CApplication.views.CreateBranchView import CreateBranchView
from C4CApplication.tests import OIDTest


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Care4Care.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^i18n/', include('django.conf.urls.i18n')),

    url(r'^admin/', include(admin.site.urls)), 
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^myc4c/$', MyCare4CareView.as_view(), name='myc4c'), 
    
    url(r'^myc4c/changeActivity$', ChangeActivityView.as_view(), name='changeActivity'),
    url(r'^myc4c/changeActivityRedirect/(?P<active>\w+)$', ChangeActivityRedirectView.as_view(), name='changeActivityRedirect'),
    url(r'^myc4c/accountstats/$', AccountStatsView.as_view(), name='accountstats'),

    url(r'^branchlist$', BranchListView.as_view(), name='branchlist'),
    url(r'^branchdetails/(?P<pk>\w+)/$', BranchDetailView.as_view(), name='branchdetails'),
    url(r'^createbranch$', CreateBranchView.as_view(), name='createbranch'),

    url(r'^logout$', LogoutView.as_view(), name='logOut'),
    url(r'^jobdetails/(?P<pk>\d+)$', JobDetailsView.as_view(), name='jobdetails'),
    url(r'^participatejob/(?P<pk>\d+)/(?P<mail>(\w+.)+\w+@(\w+.)+\w+)$', ParticipateJobRedirectView.as_view(), name='participatejob'),
    url(r'^confirmjobdone/(?P<pk>\d+)$', ConfirmJobDoneView.as_view(), name='confirmjobdone'),#not
    
    #url(r'^profile$', 'C4CApplication.views.test.profile'),
    url(r'^memberdetails/(?P<pk>(\w+.)+\w+@(\w+.)+\w+)$', MemberDetailsView.as_view(), name='memberdetails'),
    url(r'^memberdetailsredirect/(?P<pk>(\w+.)+\w+@(\w+.)+\w+)/$', MemberDetailsRedirectView.as_view(), name='memberdetailsredirect'),
    url(r'^favorites$', FavoritesView.as_view(), name='favorites'),
    url(r'^removeFavorite/(?P<pk>(\w+.)+\w+@(\w+.)+\w+)/$', RemoveFavoriteRedirectView.as_view(), name='removeFavorite'),
    url(r'^newmessage$', NewMessageView.as_view(), name='newmessage'),

    url(r'^acceptbill/(?P<pk>\d+)$', AcceptBillView.as_view(), name='acceptBill'), #not
    url(r'^confirmBill/(?P<pk>\d+)/(?P<confirm>\d+)$', ConfirmBillRedirectView.as_view(), name='confirmBill'),#not

    url(r'^transferrights/$', TransferRightsView.as_view(), name='transferrights'),
    url(r'^createbranch/$', CreateBranchView.as_view(), name='createbranch'),
    url(r'^transferrightsbranch/(?P<branch_name>\w+)/$', TransferRightsBranchView.as_view(), name='transferrightsbranch'),#not ### erreurs ###

    url(r'^deletememberbpa/$', DeleteMemberBPAView.as_view(), name='deletememberbpa'), #marche pas
    #url(r'^deletememberfrombranch/(?P<branch>\w+)/(?P<mail>(\w+.)+\w+@(\w+.)+\w+)$', DeleteMemberFromBranchRedirectView.as_view(), name='deletememberfrombranch'),

    url(r'^branchlistredirect/(?P<branch>\w+)/(?P<mail>(\w+.)+\w+@(\w+.)+\w+)/(?P<action>\d+)$', BranchListRedirectView.as_view(), name='branchlistredirect'),
    url(r'^loginasmember/(?P<mail>(\w+.)+\w+@(\w+.)+\w+)$', LoginAsMemberRedirectView.as_view(), name="loginasmember"),

    url(r'newjob/(?P<type>offer|demand)$', CreateJobView.as_view(), name='createJob'),
    url(r'donate/$', DonateTimeView.as_view(), name='donate'),
    
    url(r'^list_messages/(?P<received>\d+)$', ListMessagesView.as_view(), name='messageList'),
    url(r'^profile$', ProfileView.as_view(), name='profile'),
    url(r'^message/(?P<pk>\w+)/$', MessageView.as_view(), name='message'),
    url(r'^modifprofile/$', ModifProfileView.as_view(), name='modifprofile'),
    url(r'^modifprofileredirect/(?P<action>\d+)$', ModifProfileRedirectView.as_view(), name='modifprofileredirect'),
        
    url(r'^registration$', RegistrationView.as_view() , name='registration'),
    url(r'^registration/eidrequest$', EIDRedirectView.as_view(), name='eidrequest'),
    
    url(r'^searchjob$', SearchJobView.as_view(), name='searchjob'),

    url(r'^tests/openid$', OIDTest.oidtest), 
    url(r'^tests/openid2$', OIDTest.oidtest2)


)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
