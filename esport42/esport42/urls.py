from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from base.views import MyUserViewSet

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'esport42.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/v1/', include(router.urls)),
	url(r'', include('base.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
