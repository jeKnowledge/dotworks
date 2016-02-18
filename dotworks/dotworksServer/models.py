from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
class Company(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	company = models.CharField(max_length=100)

class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, unique = True)
	e_mail = models.EmailField(blank = False, unique = True)
	description = models.TextField(max_length = 500, blank = False)
	
	github = models.URLField(max_length=100, blank = True)
	linkdin = models.URLField(max_length=100, blank = True)
	facebook = models.URLField(max_length=100, blank = True)
	
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(validators=[phone_regex],max_length=15, blank=False) # validators should be a list
	
	name = models.CharField(max_length=100, blank = False)
	
	city = models.CharField(max_length=100, blank = False)
	country = models.CharField(max_length=100, blank = False)
	
	birth_date = models.DateField(blank = False)
	
	#Capital because of convention in django docs
	DEGREE_CHOICES = (
		("SECUNDARIO", "Secundário"),
		("LICENCIATURA", "Licenciatura"),
		("MESTRADO", "Mestrado"),
		("DOUTORAMENTO", "Doutoramento"),
	)
	degree = models.CharField(max_length=100, choices = DEGREE_CHOICES, blank = True)
	#NOT SUPPOSED TO BE BLANK=TRUE! BUG


class internship (models.Model):
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)


