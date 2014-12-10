from django.conf.urls import patterns, url

urlpatterns = patterns('',

	url(r'^tournoi/(?P<name>.*)/$', 'Tournament.views.tournoi', name='tournoi'),
	url(r'^newT$', 'Tournament.views.newT', name='newT'),
	url(r'^all$', 'Tournament.views.all', name='all'),
)
