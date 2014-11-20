from django.conf.urls import patterns, include, url
from django.contrib import admin
from C4CApplication.views.HomePageView import HomePageView
from C4CApplication.views.MyCare4CareView import MyCare4CareView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Care4Care.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomePageView.as_view(), name='home'),

    url(r'^myc4c/', MyCare4CareView.as_view(), name='myc4c'),
)
