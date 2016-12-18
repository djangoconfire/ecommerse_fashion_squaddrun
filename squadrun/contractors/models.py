from __future__ import unicode_literals
import datetime
from django.db import models
from core.models import User
# Create your models here.


class Contractor(User):
    company = models.CharField(max_length=30)
    business_area = models.CharField(max_length=50)
    billing_status = models.CharField(max_length=30)
    squad_credits = models.FloatField(default=0)