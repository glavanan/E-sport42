from django.conf.urls import patterns, url

urlpatterns = patterns('',

	url(r'^newteam/(?P<name>.*)/$', 'Team.views.newteam', name='newteam'),
)
