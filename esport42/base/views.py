from django.shortcuts import render
from django.contrib.auth.models import User
from django.forms import ModelForm
from base.models import Extend
from django import forms

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
