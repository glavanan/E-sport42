from django.db import models
from base.models import MyUser
from esport42.settings import STATIC_URL, MEDIA_URL, FRONT_POST, RULES_PATH
import os

def path_and_rename(path):
    def wrapper(instance, filename):
        filename.encode('UTF-8')
        return os.path.join(path, filename)
    return wrapper

class Tournament(models.Model):
    name = models.CharField(max_length=50, unique=True)
    tag = models.CharField(max_length=5, unique=True)
    nbteams = models.IntegerField()
    player_per_team = models.IntegerField()
    max_player = models.IntegerField()
    template = models.IntegerField()
    price = models.IntegerField()
    game_name = models.CharField(max_length=40)
    receiver_email = models.CharField(max_length=256, blank=True)
    admin = models.ManyToManyField(MyUser)
    place = models.CharField(max_length=256)
    rules = models.FileField(upload_to=path_and_rename(RULES_PATH), blank=True)


class Phase(models.Model):
    tmp_name = models.CharField(default='Tree', max_length=50)
    tournament = models.ForeignKey(Tournament)


class Teams(models.Model):
    name = models.CharField(max_length=50)
    tag = models.CharField(max_length=5)
    members = models.ManyToManyField(MyUser)
    admin = models.ForeignKey(MyUser, related_name="team_admin", null=True, blank=True)
    txn_id = models.CharField(max_length=256, blank=True)
    tournament = models.ForeignKey(Tournament)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TPost(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to=FRONT_POST)
    author = models.ForeignKey(MyUser)
    tournament = models.ForeignKey(Tournament)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '{0}'.format(self.title)


class APost(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(MyUser)
    tournament = models.ForeignKey(Tournament)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Create your models here.
