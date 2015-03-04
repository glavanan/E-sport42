from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework_nested import routers
from base.views import MyUserViewSet
from base.views import LoginView
from base.views import LogoutView


router = routers.SimpleRouter(trailing_slash=False)
router.register(r'accounts', MyUserViewSet)

urlpatterns = patterns('',
					url(r'^api/v1/', include(router.urls)),
					url(r'^api/v1/login$', LoginView.as_view(), name='login'),
					url(r'^api/v1/logout$', LogoutView.as_view(), name='logout'),
					# url(r'', include('base.urls')),
					url(r'^admin/', include(admin.site.urls)),
)
