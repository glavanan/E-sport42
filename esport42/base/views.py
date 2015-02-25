from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.forms import ModelForm
from base.models import Extend
import json
from django import forms
from django.views.generic.base import TemplateView

class TestAngular(TemplateView):
	template_name = "user/test.html"

	def get_context_data(self, **kwargs):
		context = super(TestAngular, self).get_context_data(**kwargs)
		context['latest_articles'] = ['kaka', 'hein', 'ta race']
		return context

class RegisterUserForm(ModelForm):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password']

class RegisterExtendForm(ModelForm):
	class Meta:
		model = Extend
		fields = ['address', 'nationality', 'phone']


def register(request):
	form_extend = RegisterExtendForm()
	form_user = RegisterUserForm()
	return render(request, 'user/register.html', {'form_extend' : form_extend, 'form_user' : form_user})


def endpoint(request):
	ret = {'return' : ['je', 'suis', 'des', 'donnees', 'de', 'la', 'BDD', '.']}
	return JsonResponse(ret)
