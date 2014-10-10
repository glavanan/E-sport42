from django.conf.urls import patterns, url

urlpatterns = patterns('',

	url(r'^newT$', 'Tournament.views.newT', name='newT'),
	url(r'^all$', 'Tournament.views.all', name='all'),
	url(r'^show$', 'Tournament.views.show', name='show'),
)
