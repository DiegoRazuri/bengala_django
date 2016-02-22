from __future__ import unicode_literals

from django.db import models

# Create your models here.
from enterpriseprofiles.models import Enterpriseprofile

class Award(models.Model):
	enterprise = models.ForeignKey(Enterpriseprofile, on_delete=models.CASCADE, related_name='award')
	title = models.CharField(max_length=255)
	subtitle = models.CharField(max_length=255)
	image = models.ImageField(blank=True)
	externalUrl = models.URLField(max_length=200, blank=True)

	def __str__(self):
	    return self.title

class Certification(models.Model):
	enterprise = models.ForeignKey(Enterpriseprofile, on_delete=models.CASCADE, related_name='certification')
	image = models.ImageField(blank=True)

	def __str__(self):
	    return self.enterprise.companyName