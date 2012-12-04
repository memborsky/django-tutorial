from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Poll index
    url(r'^polls/$', 'polls.views.index'),

    # Detailed poll view
    url(r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),

    # The results of the poll
    url(r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),

    # Vote on the poll
    url(r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),

    # Examples:
    # url(r'^$', 'tutorial.views.home', name='home'),
    # url(r'^tutorial/', include('tutorial.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
