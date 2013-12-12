from django.db import models

class Email(models.Model):
	Email = models.EmailField(max_length = 140)
	Password = models.CharField(max_length = 140)

	def __unicode__(self):
		return self.Email