from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(label='username',max_length=100)
	password = forms.CharField(widget=forms.PasswordInput())

class RegisterForm(forms.Form):
	name = forms.CharField(max_length=100, label="Nome Completo")
	username = forms.CharField(max_length=100, label="Introduza o seu username")
	password = forms.CharField(widget=forms.PasswordInput(), label="Introduza a sua password")
	description = forms.CharField(max_length = 500, label="Um texto sobre si [max:500car]")
	github = forms.CharField(max_length = 100, label="Github")
	linkdin = forms.CharField(max_length=100, label="Linkdin")
	facebook = forms.CharField(max_length=100, label="Facebook")
	phone = forms.CharField(max_length=100, label="Telemovel")
	city = forms.CharField(max_length=100, label="Cidade")
	country = forms.CharField(max_length=100, label="País")
	age = forms.CharField(max_length=100, label="Idade")
	degree = forms.CharField(max_length=100, label="Nivel de Educação")