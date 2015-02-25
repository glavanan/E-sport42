from django.conf.urls import patterns, url
import base.views as views

urlpatterns = patterns('base.views',
    url(r'^register$', 'register'),
    url(r'^test$', views.TestAngular.as_view(), name='test_angular'),
	url('^endpoint$', views.endpoint, name="endpoint"),
	url('^.*$', views.TestAngular.as_view(), name='test_angular'),
)
