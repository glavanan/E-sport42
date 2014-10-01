from django.conf.urls import patterns, url
from Member.views import MemberCreate

urlpatterns = patterns('',

	url(r'^accueil/$', 'Member.views.home'),
	url(r'^[/]?$', 'Member.views.home'),
	url(r'^home$', 'Member.views.home'),
	# url(r'^register$', 'Member.views.register', name='register'),
	url(r'^register[/]?$', MemberCreate.as_view(), name='register'),
	url(r'^account$', 'Member.views.my_account', name='my_account'),
	url(r'^login$', 'Member.views.login', name='login'),
	url(r'^logout$', 'Member.views.logout', name='logout'),
	url(r'^success$', 'Member.views.success', name='success'),
)
