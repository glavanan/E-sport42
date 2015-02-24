from django.conf.urls import patterns, url

urlpatterns = patterns('base.views',
		url(r'^register$', 'register'),
)
