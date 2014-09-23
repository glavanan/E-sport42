from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^accueil/$', 'Member.views.home'),
	url(r'^register$', 'Member.views.register', name='register'),
	url(r'^login$', 'Member.views.login', name='register'),
	url(r'^success$', 'Member.views.success', name='success'),
)
