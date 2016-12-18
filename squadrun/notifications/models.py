from __future__ import unicode_literals

from django.db import models
# Create your models here.


class Notification(models.Model):
    user_uuid = models.UUIDField()                # Keeping this de-normalised for performance purposes
    user_gcm = models.CharField(max_length=2048)
    text = models.CharField(max_length=255)
    read = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)  # to keep track of all notifications delevered to user