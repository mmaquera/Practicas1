from django.db import models

class AboutUs(models.Model):
	Title = models.CharField(max_length = 140)
	Description = models.TextField(max_length = 255)
	Position = models.IntegerField(default = 0)

	def __unicode__(self):
		return self.Title

class Product(models.Model):
	Name = models.CharField(max_length = 140)
	Description = models.TextField(max_length = 255)
	ImageMenu = models.ImageField(upload_to = 'imgs',verbose_name='Menu Image')
	ImagePortal = models.ImageField(upload_to = 'imgs',verbose_name='Portal Imaging')
	Position = models.IntegerField(default = 0)

	def __unicode__(self):
		return self.Name

	def getImageMenu(self):
		return self.ImageMenu

	def getImagePortal(self):
		return self.ImagePortal

class Contact(models.Model):
	Title = models.CharField(max_length = 140)
	Description = models.TextField(max_length = 255)
	Position = models.IntegerField(default = 0)

	def __unicode__(self):
		return self.Title
