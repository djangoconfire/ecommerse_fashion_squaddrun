from __future__ import unicode_literals

from django.db import models
from core.models import BaseModel
from players.models import Skills
# Create your models here.


class Mission(BaseModel):
    description = models.CharField(max_length=200)
    skills = models.ManyToManyField(Skills)
    reward = models.FloatField(default=0)
    STATUS_CHOICES = (
        ('P', 'Published'),
        ('W', 'Withdrawn'),
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    time_limit_required = models.BooleanField(default=False)
    time_limit = models.DateTimeField(default=0)
    acceptance_threshold = models.FloatField(default=0.9)     # minimum accuracy to accept mission response

# This would best be modeled in No Sql Database but to keep things simple we could use relational database as well


class Instruction(models.Model):
    mission = models.ForeignKey(Mission)
    url = models.CharField(max_length=2048)
    TYPE_CHOICES = (
        ('I', 'Image'),
        ('T', 'Text'),
        ('J', 'JSON'),
    )
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)


