from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
	user = models.OneToOneField(
		User,
		on_delete= models.CASCADE,
		primary_key=True,
	)
	companyName = models.CharField(max_length=100)
	website = models.CharField(max_length=100)


class Student(models.Model):
	user = models.OneToOneField(
		User,
		on_delete= models.CASCADE,
		primary_key=True,
	)
	decription = models.CharField(max_length=500)
	github = models.CharField(max_length=100)
	linkdin = models.CharField(max_length=100)
	facebook = models.CharField(max_length=100)
	phone = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	country = models.CharField(max_length=100)
	age = models.CharField(max_length=100)
	degree = models.CharField(max_length=100)


class internship (models.Model):
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)


