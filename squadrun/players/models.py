from __future__ import unicode_literals
import datetime
from django.db import models
# Create your models here.
from core.models import User

class Skills(models.Model):
    user = models.ForeignKey(User)
    skill_name = models.CharField(max_length=30)
    level = models.IntegerField(default=0)
    badge = models.CharField(max_length=30)


class PlayerMissions(models.Model):
    STATUS_CHOICES = (
        ('R', 'Running'),
        ('P', 'Pending Verification'),
        ('A', 'Abandoned'),
        ('D', 'Disqualified'),
    )
    started_on = models.DateTimeField(default=datetime.datetime.utcnow)
    completed_on = models.DateTimeField(default=datetime.datetime.utcnow)
    reward_earned = models.FloatField(default=0)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    missions = models.ManyToManyField('missions.Mission')


class PlayerSpecificData(models.Model):
    skills = models.ManyToManyField(Skills)
    lives = models.IntegerField(default=3)
    user = models.ForeignKey(User)
    missions = models.ManyToManyField(PlayerMissions)
    squad_coins = models.FloatField(default=0)






