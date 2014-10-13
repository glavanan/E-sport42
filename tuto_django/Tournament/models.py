#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
import math

class Team(models.Model):
	team = models.CharField(max_length=100)
	tag = models.CharField(max_length = 7)
	size = models.IntegerField()
	id_joueurs = models.ForeignKey(User)
	validate = models.CharField(max_length = 7)

class Match(models.Model):
	team1 = Team()
	team2 = Team()
	status = (
		'over',
		'pending',
		)
	winner = Team()
	score_1 = models.IntegerField()
	score_2 = models.IntegerField()

	def set_winner(self, team) :
		self.winner = team
		self.status = 'over'

	def add_team_victory(self, team) :
		if team == self.team1 :
			self.score_1 = self.score_1 + 1
		elif team == self.team2 :
			self.score_2 = self.score_2 + 1
		else :
			return "cette team ne joue pas dans ce match"

	def init_match(self, team1, team2) :
		self.team1 = team1
		self.team2 = team2
		score_2 = 0;
		score_1 = 0;
		status = 'pending'



class Tournament(models.Model):
	nb_team = models.IntegerField()
	nb_joueur = models.IntegerField()
	nom = models.CharField(max_length = 100)
	tag = models.CharField(max_length = 10)
	etat = models.CharField(max_length = 30)
	description = models.TextField()
	jeu = models.CharField(max_length = 30)
	image = models.CharField(max_length = 30)
	template = models.CharField(max_length = 30)
	prix = models.IntegerField()
	matchs = {}
	nb_round = 0
	
	def __unicode__(self):
		return u"%s" % self.nom

	def init_tourn(self):
		self.nb_round = int(math.ceil(math.log(self.nb_team,2)))
		for i in range(1, pow(2, self.nb_round - 1) + 1) :
			self.matchs[i] = "Match()"

	def change_match(self, first, second):
		save = self.matchs[first]
		self.matchs[first] = self.matchs[second]
		self.matchs[second] = save

	def next_match(self, cur_round, cur_match) :
		if cur_round != self.nb_round :
			if (cur_match % 2) == 1 :
				if self.matchs[cur_match + 1].status == "over" :
					self.matchs[pow(2, self.nb_round - 1) + (cur_match + 1) / 2] = Match()
			else :
				if self.matchs[cur_match - 1].status == "over" :
					self.matchs[pow(2, self.nb_round - 1) + cur_match / 2] = Match()
		else :
			return "no next match"

# Create your models here.
