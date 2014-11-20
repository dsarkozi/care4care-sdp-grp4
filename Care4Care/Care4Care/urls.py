from django.conf.urls import patterns, include, url
from django.contrib import admin
from C4CApplication.views.HomePageView import HomePageView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Care4Care.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomePageView.as_view(), name='home'),
)
