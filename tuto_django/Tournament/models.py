#-*- coding: utf-8 -*-
from django.db import models

class Tournament(models.Model):
	nb_team = models.IntegerField()
	nb_joueur = models.IntegerField()
	nb_remplace = models.IntegerField(default = 0)
	nom = models.CharField(max_length = 100)
	tag = models.CharField(max_length = 10)
	etat = models.CharField(max_length = 30)
	description = models.TextField()
	jeu = models.CharField(max_length = 30)
	image = models.CharField(max_length = 30)
	template = models.CharField(max_length = 30)
	prix = models.IntegerField()
	
	def __unicode__(self):
		return u"%s" % self.nom
# Create your models here.
