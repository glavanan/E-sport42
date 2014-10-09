from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tuto_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


	url(r'', include('Member.urls')),
	url(r'', include('Tournament.urls')),
	url(r'^admin/', include(admin.site.urls)),
)
