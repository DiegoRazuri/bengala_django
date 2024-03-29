from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Enterpriseprofile(models.Model):
	companyName = models.CharField(max_length=255)
	descriptor = models.CharField(max_length=255, blank=True)
	profileImage = models.ImageField(blank=True, default='Equipo.jpg')
	bannerImage = models.ImageField(blank=True, default='Equipo.jpg')
	businessName = models.CharField(max_length=255)
	industry = models.CharField(max_length=255)
	legalId = models.CharField(max_length=11, unique=True)
	phone = models.PositiveIntegerField()
	email = models.EmailField(max_length=255, blank=True)
	web = models.URLField(max_length=200, blank=True)
	address = models.CharField(max_length=255, blank=True)
	us = models.CharField(max_length=600, blank=True)
	offer = models.CharField(max_length=600, blank=True)
	relationship = models.ManyToManyField('self', through='Client', blank=True, symmetrical=False, related_name='related_to',)
	searchKeywords = models.CharField(max_length=180, blank=True)
	facebookURL = models.URLField(max_length=200, blank=True)
	twitterURL = models.URLField(max_length=200, blank=True)
	instagramURL = models.URLField(max_length=200, blank=True)
	youtubeURL = models.URLField(max_length=200, blank=True)

	def __str__(self):
	    return self.companyName
	def __unicode__(self):
		return self.companyName

	def add_client(self, enterprise, status):
		relationship, created = relationship.objects.get_or_create(
			from_enterprise = self,
			to_enterprise = enterprise,
			status = status)
		return relationship

	def add_provider(self, enterprise, status):
		relationship, created = relationship.objects.get_or_create(
			from_enterprise = enterprise,
			to_enterprise = self,
			status = status)
		return relationship

	def remove_client(self, enterprise, status):
		relationship.objects.filter(
			from_enterprise =self,
			to_enterprise=enterprise,
			status=status).delete()
		return

	def remove_provider(self, enterprise, status):
		relationship.objects.filter(
			from_enterprise = enterprise,
			to_enterprise=self,
			status=status).delete()
		return

	def get_clients(self, status):
		return self.relationship.filter(
			to_enterprises__status=status,
			to_enterprises__from__enterprise=self)

	def get_related_to(self, status):
		return self.related_to.filter(
			from_enterprises__status = status,
			from_enterprises__to_enterprise = self)

	def get_following_clients(self):
		return self.get_clients(RELATIONSHIP_FOLLOWING)

	def get_followers_providers(self):
		return self.get_related_to(RELATIONSHIP_FOLLOWING)

	def get_friends(self):
		return self.client.filter(
			to_enterprises__status=RELATIONSHIP_FOLLOWING,
			to_enterprises__from__enterprise=self,
			from_enterprises__status= RELATIONSHIP_FOLLOWING,
			from_enterprises__to_enterprise=self)

RELATIONSHIP_FOLLOWING = 1
RELATIONSHIP_BLOCKED = 2
RELATIONSHIP_STATUSES = (
	(RELATIONSHIP_FOLLOWING, 'Following'),
	(RELATIONSHIP_BLOCKED, 'Blocked'),
)

class Client(models.Model):
	enterprise = models.ForeignKey(Enterpriseprofile, related_name="relations")
	client = models.ForeignKey(Enterpriseprofile, related_name="to_enterprise")
	status = models.IntegerField(choices=RELATIONSHIP_STATUSES)
'''
class Provider(models.Model):
	enterprise = models.ForeignKey(Enterpriseprofile, related_name="from_enterprise_p")
	provider = models.ForeignKey(Enterpriseprofile, related_name="to_enterprise_p")
	status = models.IntegerField(choices=RELATIONSHIP_STATUSES)'''