from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework_nested import routers
from base.views import MyUserViewSet


router = routers.SimpleRouter(trailing_slash=False)
router.register(r'accounts', MyUserViewSet)

urlpatterns = patterns('',
					   url(r'^api/v1/', include(router.urls)),
					   # url(r'', include('base.urls')),
					   url(r'^admin/', include(admin.site.urls)),
)
