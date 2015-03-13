from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager

class AccountManager(BaseUserManager):
    def create_user(self, username, password=None, **kwargs):
        if not kwargs.get('email'):
            raise ValueError('User must have a valid email')
        if not username:
            raise ValueError('User must have a valid username')
        account = self.model(username=username, email=self.normalize_email(kwargs.get('email')),
                             first_name=kwargs.get('first_name', ''), last_name=kwargs.get('last_name', ''),
                             address=kwargs.get('address', ''), birth_date=kwargs.get('birth_date'), nationality=kwargs.get('nationality', 'FR'), phone=kwargs.get('phone', ''))
        account.set_password(password)
        account.save()
        return account
    def create_superuser(self, username, password, **kwrags):
        account = self.create_user(username, password, **kwrags)
        account.set_password(password)
        account.is_admin = True
        account.is_staff = True
        account.save()
        return account

class Teams(models.Model):
    name = models.CharField(max_length=50)

class MyUser(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    address = models.TextField(blank = True)
    birth_date = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=40, blank=True, default='FR')
    phone = models.CharField(max_length = 14, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    teams = models.ManyToManyField(Teams)
    objects = AccountManager()
    def __unicode__(self):
        return self.username

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name


