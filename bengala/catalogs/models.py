from __future__ import unicode_literals

from django.db import models
from enterpriseprofiles.models import Enterpriseprofile

# Create your models here.
class Catalog(models.Model):
	enterprise = models.ForeignKey(Enterpriseprofile, on_delete=models.CASCADE, related_name='catalog')
	image = models.ImageField(blank=True)
	title = models.CharField(max_length=255)
	subtitle = models.CharField(max_length=255)
	description = models.TextField(max_length=500)


	def __str__(self):
	    return self.title