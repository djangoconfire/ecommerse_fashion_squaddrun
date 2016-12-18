from __future__ import unicode_literals

from django.db import models

class Ecommerse(models.Model):
	laptop	=models.FileField(upload_to="ecommerse/images")


	def __unicode__(self):
		return self.laptop

		



