from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
	email = models.CharField(max_length=200)
	password = models.CharField(max_length=200)

#class Company(models.Model):
#	companyUser= models.User()
	#atributos


#class Student(models.Model):
	#atributos



