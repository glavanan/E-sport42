#-*- coding: utf-8 -*-
from django.db import models

class Team(models.Model):
	team = models.CharField(max_length=100)
	tag = models.CharField(max_length = 7)
	size = models.IntegerField()
	id_joueurs = models.ForeignKey(User)
	validate = models.CharField()
	id_tournament = models.ForeignKey(Tournament)

# Create your models here.
