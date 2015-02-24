from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from base.models import Extend
from django import forms
from django.contrib.auth import authenticate

class RegisterUserForm(ModelForm):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password']

class RegisterExtendForm(ModelForm):
	class Meta:
		model = Extend
		fields = ['address', 'nationality', 'phone', 'birth_date']

def register(request):
	if request.method == 'POST':
		form_user = UserCreationForm(request.POST)
		if form_user.is_valid():
			user = form_user.save()
			user.save()
			loged = authenticate(username=user.username, password=user.password)
			if user is not None:
				login(request, loged)
				return render(request, 'user/account.html')
				print("log")
			else:
				print("notlog")
		return render(request, 'user/register.html', {'form_user' : form_user})
	form_user = UserCreationForm()
	return render(request, 'user/register.html', {'form_user' : form_user})

