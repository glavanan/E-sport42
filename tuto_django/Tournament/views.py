from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django import forms
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext
from models import Tournament
from django.utils import unittest

class TournamentForm(forms.Form):
	nb_team = forms.IntegerField(required = True)
	nb_joueur = forms.IntegerField(required = True)
	nom = forms.CharField(required = True, max_length = 100)
	tag = forms.CharField(required = True, max_length = 10)
	etat = forms.CharField(required = True, max_length = 30)
	description = forms.CharField(required = True)
	jeu = forms.CharField(required = True, max_length = 30)
	image = forms.CharField(max_length = 30, required=False)
	template = forms.CharField(max_length = 30, required=False)
	prix = forms.IntegerField(required = True)

def newT(request):
	text = "RIEN"
	tournament_form = TournamentForm()
	if request.user.is_superuser or True:
		text = "SUPERUSER"
		if request.method == 'POST':
			text = "POST"
			tournament_form=TournamentForm(request.POST)
			if tournament_form.is_valid():
				text = "VALIDE"
				tags = tournament_form.cleaned_data['tag']
				print tags
				if Tournament.objects.filter(tag = tags).count():
					text = "Deja utiliser il faut un unique TAG (NOOOOOOB!)"
				else:
					newT = Tournament(nb_team = tournament_form.cleaned_data['nb_team'], nb_joueur = tournament_form.cleaned_data['nb_joueur'], nom = tournament_form.cleaned_data['nom'], tag = tournament_form.cleaned_data['tag'], etat = tournament_form.cleaned_data['etat'], description = tournament_form.cleaned_data['description'], jeu = tournament_form.cleaned_data['jeu'],image = tournament_form.cleaned_data['image'],template =  tournament_form.cleaned_data['template'], prix =  tournament_form.cleaned_data['prix'])
					newT.init_tourn()
					newT.save()
					return render_to_response('Tournament/show.html', {'matchs' : newT.matchs}, context_instance=RequestContext(request))
		return render_to_response('Tournament/newT.html', {'Tournament_form' : tournament_form, 'message' : text}, context_instance=RequestContext(request))

def all(request):
	liste = list()
	liste_tournois = Tournament.objects.all()
	print liste_tournois
	for tournoi in liste_tournois:
		print tournoi
		liste.append(tournoi)
	return render_to_response('Tournament/all.html',{'tag' : liste}, context_instance=RequestContext(request))

def show(request, name):
	tournament = Tournament()
	try :
		tournament = Tournament.objects.get(nom = name)
	except tournament.DoesNotExist :
		text = "Ce tournoi n'existe pas renseigner un autre nom"
		liste = list()
		liste_tournois = Tournament.objects.all()
		print liste_tournois
		for tournoi in liste_tournois:
			print tournoi
			liste.append(tournoi)
		return render_to_response('Tournament/all.html',{'tag' : liste, 'message' : text}, context_instance=RequestContext(request))
	return render_to_response('Tournament/show.html',{'matchs' : tournament.matchs}, context_instance=RequestContext(request))