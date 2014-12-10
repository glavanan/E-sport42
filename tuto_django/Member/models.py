#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from Team.models import Team

class Member(models.Model):
	user = models.OneToOneField(User)
	age = models.IntegerField()
	pays = models.CharField(max_length=30)
	ville = models.CharField(max_length=60)
	adresse = models.TextField()
	mail = models.CharField(max_length=511)
	pseudo_lol = models.CharField(max_length=30)
	duoquadra = models.CharField(max_length=10)
	team = models.ManyToManyField(Team)
	
	def __unicode__(self):
		return u"%s" % self.user
# Create your models here.
