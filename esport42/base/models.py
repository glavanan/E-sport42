from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.contrib.auth.models import AbstractBaseUser


class Teams(models.Model):
	name = models.CharField(max_length = 50)

class MyUser(AbstractBaseUser):
	address = models.CharField(max_length = 255, blank = True)
	birth_date = models.DateField()
	nationality = CountryField()
	phone = models.IntegerField()
	REQUIRED_FIELDS = ['nationality', 'birth_date', 'address']
	teams = models.ManyToManyField(Teams)


# Create your models here.
