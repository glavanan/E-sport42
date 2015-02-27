from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager

class AccountManager(BaseUserManager):
    def create_user(self, username, **kwargs):
        if not username:
            raise ValueError('Username doit etre valide')
        if not kwargs.get('password1'):
            raise ValueError('password et confirmation doivent etre remplis')
        if not kwargs.get('password2'):
            raise ValueError('password et confirmation doivent etre remplis')
        if kwargs.get('password1') != kwargs.get('password2'):
            raise ValueError('password et confirmation doivent etre remplis et identique')
        if not kwargs.get('email'):
            raise ValueError('email non valide')
        if not kwargs.get('first_name'):
            raise ValueError('On a besoins du Nom et Prenom')
        if not kwargs.get('last_name'):
            raise ValueError('On a besoins du Nom et Prenom')
        if not kwargs.get('nationality'):
            raise ValueError('On a besoins de savoir ou tu habite')
        if not kwargs.get('address'):
            raise ValueError('On a besoins de savoir ou tu habite')
        if not kwargs.get('birth_date'):
            raise ValueError('On a besoins de savoir ou tu habite')
        account = self.model(username=username, email=self.normalize_email(kwargs.get('email')), first_name=kwargs.get('first_name'),
                             last_name=kwargs.get('last_name'), nationality=kwargs.get('nationality'),
                             address=kwargs.get('address'), birth_date=kwargs.get('birth_date'),
                             phone=kwargs.get('phone'))
        account.set_password(kwargs.get('password1'))
        account.save()
        return account
    def create_superuser(self, username, **kwrags):
        account = self.create_user(username, **kwrags)
        account.is_admin = True
        account.save()

        return account

class Teams(models.Model):
    name = models.CharField(max_length = 50)

class MyUser(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    address = models.TextField(blank = True)
    birth_date = models.DateField()
    nationality = CountryField()
    phone = models.CharField(max_length = 14, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'nationality', 'birth_date', 'address']
    teams = models.ManyToManyField(Teams)
    objects = AccountManager()
    def __unicode__(self):
        return self.username

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name


# Create your models here.
