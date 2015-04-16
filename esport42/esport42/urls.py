from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework_nested import routers
from base.views import MyUserViewSet, IndexView
from tournoi.views import TournamentViewSet, TeamsViewSet
from post.views import PostViewSet
router = routers.SimpleRouter(trailing_slash=False)
router.register(r'accounts', MyUserViewSet)
#<<<<<<< HEAD
router.register(r'post', PostViewSet)
router.register(r'tournoi', TournamentViewSet)
router.register(r'teams', TeamsViewSet)
#=======
#router.register(r'posts', PostViewSet)
#
#>>>>>>> c8a472929faf4e055c78c41c14c52c4126102fe9
urlpatterns = patterns('',
					url(r'^api/v1/', include(router.urls)),
					url(r'^api/v1/', include('base.urls')),
					# url(r'^admin/', include(admin.site.urls)),
                    url(r'^.*$', IndexView.as_view())
)
