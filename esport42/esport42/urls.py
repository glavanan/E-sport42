from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework_nested import routers
from base.views import MyUserViewSet, IndexView, TournamentViewSet, TeamsViewSet
from post.views import PostViewSet
router = routers.SimpleRouter(trailing_slash=False)
router.register(r'accounts', MyUserViewSet)
router.register(r'post', PostViewSet)
router.register(r'tournoi', TournamentViewSet)
router.register(r'teams', TeamsViewSet)
urlpatterns = patterns('',
					url(r'^api/v1/', include(router.urls)),
					url(r'^api/v1/', include('base.urls')),
					# url(r'^admin/', include(admin.site.urls)),
                    url(r'^.*$', IndexView.as_view())
)
