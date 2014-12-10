#-*- coding: utf-8 -*-
from django.db import models
from Tournament.models import Tournament
from django.contrib.auth.models import User

class Team(models.Model):
	team = models.CharField(max_length=100)
	tag = models.CharField(max_length = 7)
	size = models.IntegerField()
	validate = models.IntegerField()
	id_tournament = models.ForeignKey(Tournament)

# Create your models here.
