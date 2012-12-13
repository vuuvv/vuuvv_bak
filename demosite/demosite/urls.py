from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from vuuvv.dashboard.views import Login

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'vuuvv.themes.views.home', name='home'),
    url(r'^login/$', Login.as_view(), name='login'),
    # url(r'^demosite/', include('demosite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
