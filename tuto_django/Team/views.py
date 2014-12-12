from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django import forms
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext
from models import Tournament
from models import Team

class TeamForm(forms.Form):
	team = forms.CharField(max_length=100)
	tag = forms.CharField(max_length=7)
	
	def __init__(self, *args, **kwargs):
		index = 0
		players = kwargs.pop('size')
		bonnus = kwargs.pop('supp')
		print type(players)
		super(TeamForm, self).__init__(*args, **kwargs)
		while index < players:
			self.fields['player_{index}'.format(index=index)] = forms.CharField(required = True)
			index = index+1
		while index < bonnus + players:
			self.fields['player_{index}'.format(index=index)] = forms.CharField(required = False)
			index = index+1


def newteam(request, name):
	text = ""
	tournois = Tournament.objects.get(nom = name)
	team_form=TeamForm(size = tournois.nb_joueur,supp = tournois.nb_remplace)
	if request.user.is_authenticated():
		if request.method == "POST":
			team_form = TeamForm(request.POST, size=tournois.nb_joueur,supp=tournois.nb_remplace)
			if team_form.is_valid():
				index = 0
				error_list = str()
				pseudo = list()
				base = list()
				while index < tournois.nb_joueur + tournois.nb_remplace:
					pseudo.append(request.POST.get("player_" + str(index)))
					index = index+1
				result = list()
				doublon = list()
				existe = User.objects.filter(username__in=pseudo).values_list('username')
				for string in existe:
					for word in string:
						base.append(str(word))
				for string in pseudo:
					if string not in result and string in base:
						result.append(string)
					else:
						doublon.append(string)
				
				print result
				print doublon
				if len(doublon) > 0:
					text = "Error : " + ", ".join(doublon) + " sont des doublon ou ces joueurs n'existe pas"  
		else:
			team_form = TeamForm(size = tournois.nb_joueur,supp=tournois.nb_remplace)
	return render_to_response("Team/newteam.html", {'form' : team_form, 'name' : name, 'text' : text}, context_instance=RequestContext(request))
	print "OK"
	

# Create your views here.
