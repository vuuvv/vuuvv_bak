from django.conf.urls import patterns, include, url

from vuuvv.dashboard.views import Main

urlpatterns = patterns('',
    url(r'^$', Main.as_view(), name='main'),
)
