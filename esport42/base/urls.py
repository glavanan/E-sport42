from django.conf.urls import patterns, url
import base.views as views

urlpatterns = patterns('base.views',
    url(r'login$', views.LoginView.as_view(), name='login'),
    url(r'logout$', views.LogoutView.as_view(), name='logout'),
    url(r'username-exists$', views.UserExists.as_view(), name='uexists'),
    url(r'email-exists$', views.EmailExists.as_view(), name='eexists')
)
