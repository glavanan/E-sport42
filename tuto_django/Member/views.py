#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.forms import ModelForm
from django.shortcuts import render_to_response, HttpResponseRedirect
from models import Member
from django.contrib.auth.models import User
from django import forms
from django.template import RequestContext
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

class MemberForm(ModelForm):
	class Meta:
		model = Member

class UserForm(forms.Form):
	username = forms.CharField(required=True, max_length=30)
	first_name = forms.CharField(label = 'Nom', required=True, max_length=30)
	last_name = forms.CharField(label = 'Prenom', required=True, max_length=30)
	password = forms.CharField(widget=forms.PasswordInput, required=True, max_length=255)
	email = forms.EmailField(required=True)

def home(request):
	return render_to_response('Member/home.html')

def register(request):
	text = ""
	if request.method == 'POST':
		member_form = UserForm(request.POST)
		if member_form.is_valid():
			name = member_form.cleaned_data['username']
			if User.objects.filter(username = name).count():
				text = "usename deja utilisee !"
			else:
				user = User.objects.create_user(name, member_form.cleaned_data['email'], member_form.cleaned_data['password'], first_name = member_form.cleaned_data['first_name'], last_name = member_form.cleaned_data['last_name'])
				return HttpResponseRedirect('/success')
	else:
		member_form = UserForm()

	return render_to_response('Member/register.html', {'member_form' : member_form, 'message' : text}, context_instance=RequestContext(request))

class LoginForm(forms.Form):
	username = forms.CharField(required=True, max_length=30)
	password = forms.CharField(widget=forms.PasswordInput, max_length=30, required=True)

def login(request):
	text = ""
	login_form = LoginForm()
	if not request.user.is_authenticated():
		if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
	
			if user is not None:
				auth_login(request, user)
				return HttpResponseRedirect('/success')
				
			else:
				text = "mauvais mots de passe ou nom d'utilisateur"
				return render_to_response('Member/login.html', {'login_form' : login_form, 'message' : text}, context_instance=RequestContext(request))
		else:
			return render_to_response('Member/login.html', {'login_form' : login_form, 'message' : text}, context_instance=RequestContext(request))
	else:
		return render_to_response('Member/home.html')

def logout(request):
	auth_logout(request)
	login_form = LoginForm()
	text = ""
	return render_to_response('Member/login.html', {'login_form' : login_form, 'message' : text}, context_instance=RequestContext(request))

def success(request):
	return HttpResponse('<p>Success</p>')
# Create your views here.
