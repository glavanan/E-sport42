from django.db import models
from tournoi.models import Teams, Phase

# Create your models here.
class Match(models.Model):
    team1 = models.ForeignKey(Teams, related_name='team1', null=True)
    team2 = models.ForeignKey(Teams, related_name='team2', null=True)
    phase = models.ForeignKey(Phase, related_name='phase')
    score_t1 = models.IntegerField(default=0, null=True)
    score_t2 = models.IntegerField(default=0, null=True)
    end = models.BooleanField(default=False)
    looser_braket=models.BooleanField(default=False)
    level = models.IntegerField(default=0)
    match_number = models.IntegerField(default=0)