# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.core.urlresolvers import reverse


class Quadra(models.Model):
	is_42 = models.BooleanField(default=False)
	login = models.CharField(max_length=10, null=True)


class Member(models.Model):
	user = models.OneToOneField(User)
	quadra = models.OneToOneField(Quadra)
	age = models.PositiveSmallIntegerField(null=True)
	country = CountryField(null=True)
	city = models.CharField(max_length=60, null=True)
	address = models.CharField(max_length=200, null=True)
	mail = models.EmailField(unique=True, null=True)
	registration_date = models.DateField(auto_now_add=True, null=True)
	pseudo = models.CharField(max_length=30, null=True)

	def get_absolute_url(self):
		return reverse('member-detail', kwargs={'pk': self.pk})

	def __unicode__(self):
		return u"%s" % self.titre
