from django.conf.urls import patterns, url
from tournoi.views import ipn, ipn_return ,TeamExists, TagExists
import base.views as views

urlpatterns = patterns('base.views',
    url(r'^login$', views.LoginView.as_view(), name='login'),
    url(r'^logout$', views.LogoutView.as_view(), name='logout'),
    url(r'^username-exists$', views.UserExists.as_view(), name='uexists'),
    url(r'^email-exists$', views.EmailExists.as_view(), name='eexists'),
    url(r'^team-exists$', TeamExists.as_view(), name="ttexists"),
    url(r'^tag-exists$', TagExists.as_view(), name="ttexists"),
    url(r'^ipn$', view=ipn),
    url(r'^ipn-return$', view=ipn_return, name="ipn_return"),
    url(r'^.*$', views.NotFound.as_view(), name='notfound')
)
