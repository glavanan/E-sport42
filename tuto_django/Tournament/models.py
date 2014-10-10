#-*- coding: utf-8 -*-
from django.db import models
import math

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
			self.matchs[i] = "match numéro " + str(i) + " du 1er round"

	def change_match(self, first, second):
		save = self.matchs[first]
		self.matchs[first] = self.matchs[second]
		self.matchs[second] = save

	def next_match(self, cur_round, cur_match) :
		self.matchs[cur_match].status = "over"
		if cur_round != self.nb_round :
			if (cur_match % 2) == 1 :
				if self.matchs[cur_match + 1].status == "over" :
					self.matchs[pow(2, self.nb_round - 1) + (cur_match + 1) / 2] = "match suivant"
			else :
				if self.matchs[cur_match - 1].status == "over" :
					self.matchs[pow(2, self.nb_round - 1) + cur_match / 2] = "match suivant"
		else :
			return "no next match"

# Create your models here.
