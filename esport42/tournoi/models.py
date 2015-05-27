from django.db import models
from base.models import MyUser
from esport42.settings import STATIC_URL, MEDIA_URL, FRONT_POST

class Tournament(models.Model):
    name = models.CharField(max_length=50)
    nbteams = models.IntegerField()
    player_per_team = models.IntegerField()
    template = models.IntegerField()
    price = models.IntegerField()
    receiver_email = models.CharField(max_length=256, blank=True)
    admin = models.ManyToManyField(MyUser)

class Phase(models.Model):
    tmp_name = models.CharField(default='Tree', max_length=50)
    tournament=models.ForeignKey(Tournament)

class Teams(models.Model):
    name = models.CharField(max_length=50, unique=True)
    tag = models.CharField(max_length=5, unique=True)
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
