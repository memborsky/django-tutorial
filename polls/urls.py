from django.conf.urls import patterns, include, url

urlpatterns = patterns('polls.views',
    # Poll index
    url(r'^$', 'index'),

    # Detailed poll view
    url(r'^(?P<poll_id>\d+)/$', 'detail'),

    # The results of the poll
    url(r'^(?P<poll_id>\d+)/results/$', 'results'),

    # Vote on the poll
    url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
)
