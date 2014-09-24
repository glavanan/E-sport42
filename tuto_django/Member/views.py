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


class AccountForm(forms.Form):
	def __init__(self, *args, **kwargs):
		request=kwargs.pop("first_name")
		pays = kwargs.pop("pays")
		super(AccountForm, self).__init__(*args, **kwargs)
		self.fields['first_name'] = forms.CharField(label = 'Nom', required=True, max_length=30, initial=request)
#	last_name = forms.CharField(label = 'Prenom', required=True, max_length=30, value=request.user.last_name)
#	email = forms.EmailField(required=True, value=str(request.user.email))
#		self.fields['age'] = forms.IntegerField(initial=age, required=False)
	      	self.fields['pays'] = forms.CharField(max_length=30, initial=pays, required=False)
   #     ville = forms.CharField(max_length=60, value=request.user.ville)
    #    adresse = forms.TextField(value=request.user.adresse)
     #   pseudo_lol = forms.CharField(max_length=30, value=request.user.pseudo_lol)
      #  duoquadra = forms.CharField(max_length=10, value=request.user.duoquadra)
	
class UserForm(forms.Form):
	username = forms.CharField(required=True, max_length=30)
	first_name = forms.CharField(label = 'Nom', required=True, max_length=30)
	last_name = forms.CharField(label = 'Prenom', required=True, max_length=30)
	password = forms.CharField(widget=forms.PasswordInput, required=True, max_length=255)
	email = forms.EmailField(required=True)

def home(request):
	return render_to_response('Member/home.html', {'user' : request.user.username})

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
		return render_to_response('Member/home.html', {'user' : request.user.username})

def logout(request):
	auth_logout(request)
	login_form = LoginForm()
	text = ""
	return render_to_response('Member/login.html', {'login_form' : login_form, 'message' : text}, context_instance=RequestContext(request))

def my_account(request):
	text = ""
	member = Member(user=request.user)
	account_form=AccountForm(first_name = request.user.first_name, pays = request.user.member.pays)
	if request.method == 'POST':
		if account_form.is_valid():
			text="VALIDE"
			user.first_name, user.age = account_form.cleaned_data['first_name'], account_form.cleaned_data['pays']
		else:
			print account_form.errors
			text=account_form.errors
			return render_to_response('Member/account.html', {'account_form' : account_form, 'message' : text}, context_instance=RequestContext(request))
	else:
		if request.user.is_authenticated():
			return render_to_response('Member/account.html', {'account_form' : account_form, 'message' : text}, context_instance=RequestContext(request))
		else:
			return render_to_response('Member/home.html', {'user' : request.user.username})


def success(request):
	return HttpResponse('<p>Success</p>')
# Create your views here.
