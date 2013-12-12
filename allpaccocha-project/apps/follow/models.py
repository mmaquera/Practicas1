from django.db import models

class Blogger(models.Model):
	Url = models.URLField(max_length = 140)

	def __unicode__(self):
		return self.Url

class Facebook(models.Model):
	Url = models.URLField(max_length = 140)

	def __unicode__(self):
		return self.Url

class Twitter(models.Model):
	Url = models.URLField(max_length = 140)

	def __unicode__(self):
		return self.Url