from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class Teams(models.Model):
	name = models.CharField(max_length = 50)

class Extend(models.Model):
	user = models.OneToOneField(User)
	nickname = models.CharField(max_length = 50)
	address = models.CharField(max_length = 255, blank = True)
	birth_date = models.DateField()
	nationality = CountryField()
	phone = models.IntegerField()
	teams = models.ManyToManyField(Teams)


# Create your models here.
