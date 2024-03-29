from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework_nested import routers
from base.views import MyUserViewSet, IndexView, HomeView
from tournoi.views import TournamentViewSet, TeamsViewSet, TPostViewSet, APostViewSet, ipn, ipn_test
from post.views import PostViewSet
from match.views import MatchViewSet
from rest_framework_extensions.routers import ExtendedSimpleRouter

router = ExtendedSimpleRouter(trailing_slash=False)
router.register(r'accounts', MyUserViewSet)
router.register(r'tournoi', TournamentViewSet).register(r'posts', TPostViewSet, base_name="TPost", parents_query_lookups=['tournoi'])
router.register(r'tournoi', TournamentViewSet).register(r'article', APostViewSet, base_name="APost", parents_query_lookups=['tournoi'])
router.register(r'tournoi', TournamentViewSet).register(r'team', TeamsViewSet, base_name="team", parents_query_lookups=['tournoi']).register(r'match', MatchViewSet, base_name='Match', parents_query_lookups=['tournoi', 'phase'])
router.register(r'posts', PostViewSet)

urlpatterns = patterns('',
					url(r'^api/v1/', include(router.urls)),
					url(r'^api/ret/ipn', view = ipn),
					url(r'^api/v1/', include('base.urls')),
                    url(r'^home$', HomeView.as_view()),
                    url(r'^.*$', IndexView.as_view())

)
