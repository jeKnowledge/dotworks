from django import forms
from .models import Student
import datetime

class LoginForm(forms.Form):
	username = forms.CharField(label='username',max_length=100)
	password = forms.CharField(widget=forms.PasswordInput())

class StudentRegisterForm(forms.Form):
	name = forms.CharField(max_length=100, label="Nome Completo", required = True)
	email = forms.EmailField(required = True)
	password = forms.CharField(widget=forms.PasswordInput(), label="Introduza a sua password", required = True)
	description = forms.CharField(widget= forms.Textarea, max_length = 500, label="Um texto sobre si [max:500car]", required = True)
	github = forms.URLField(max_length = 100, label="Github", required = False)
	linkdin = forms.URLField(max_length=100, label="Linkdin", required = False)
	facebook = forms.URLField(max_length=100, label="Facebook", required = False)
	phone = forms.RegexField(regex=r'^\+?1?\d{9,15}$', max_length=15, min_length=9, label="Telemovel", required = True)
	city = forms.CharField(max_length=100, label="Cidade", required = True)
	country = forms.CharField(max_length=100, label="País", required = True)
	birth_date = forms.DateField(widget=forms.DateInput(),label="Data nascimento", required = True, initial=datetime.date.today)
	degree = forms.ChoiceField(choices = Student.DEGREE_CHOICES, required = False)