#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.forms import ModelForm
from django.shortcuts import render_to_response, HttpResponseRedirect
from models import Member
from django.contrib.auth.models import User
from django import forms
from django.template import RequestContext

class MemberForm(ModelForm):
	class Meta:
		model = Member

class UserForm(forms.Form):
	username = forms.CharField(required=True, max_length=30)
	first_name = forms.CharField(label = 'Nom', required=True, max_length=30)
	last_name = forms.CharField(label = 'Prenom', required=True, max_length=30)
	password = forms.CharField(required=True, max_length=255)
	email = forms.EmailField(required=True)

def home(request):
  text = """<h1>Bienvenue sur mon blog !</h1>
            <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>"""
  return HttpResponse(text)

def register(request):
	if request.method == 'POST':
		member_form = UserForm(request.POST)
		if member_form.is_valid():
			user = User.objects.create_user(member_form.cleaned_data['username'], member_form.cleaned_data['email'], member_form.cleaned_data['password'], first_name = member_form.cleaned_data['first_name'], last_name = member_form.cleaned_data['last_name'])
			return HttpReponseRedirect('/success')
	else:
		member_form = UserForm()

	return render_to_response('Member/register.html', {'member_form' : member_form}, context_instance=RequestContext(request))

def success(request):
    return HttpResponse('<p>Success</p>')
# Create your views here.
