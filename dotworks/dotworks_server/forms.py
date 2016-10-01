# coding=utf-8
import datetime
from django import forms
from .models import Student


class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class StudentRegisterForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Nome Completo",
        required=True
    )
    email = forms.EmailField(required=True)
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label="Introduza a sua password",
        required=True
    )
    description = forms.CharField(
        widget=forms.Textarea,
        max_length=500,
        label="Um texto sobre si [max:500car]",
        required=True
    )
    github = forms.URLField(max_length=100, label="Github", required=False)
    linkedin = forms.URLField(max_length=100, label="Linkdin", required=False)
    facebook = forms.URLField(
        max_length=100,
        label="Facebook",
        required=False
    )
    phone = forms.RegexField(
        regex=r'^\+?1?\d{9,15}$',
        max_length=15,
        min_length=9,
        label="Telemovel",
        required=True
    )
    city = forms.CharField(max_length=100, label="Cidade", required=True)
    country = forms.CharField(max_length=100, label="Pais", required=True)
    birth_date = forms.DateField(
        widget=forms.DateInput(),
        label="Data nascimento",
        required=True,
        initial=datetime.date.today
    )
    degree = forms.ChoiceField(
        choices=Student.DEGREE_CHOICES,
        required=True
    )


class CompanyRegisterForm(forms.Form):
    company = forms.CharField(
        max_length=100,
        label="Nome da Companhia",
        required=True
    )
    email = forms.EmailField(required=True)
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label="Password",
        required=True
    )
    description = forms.CharField(
        widget=forms.Textarea,
        max_length=500,
        label="Descricao[500car]",
        required=True
    )

    site = forms.URLField(
        max_length=100,
        label="Site da empresa",
        required=True
    )
    facebook = forms.URLField(max_length=100, label="Facebook", required=False)
    phone = forms.RegexField(
        regex=r'^\+?1?\d{9,15}$',
        max_length=15,
        min_length=9,
        label="Telemovel",
        required=True
    )


class InternshipCreationForm(forms.Form):
    title = forms.CharField(max_length=100, label="Titulo do estágio")
    description = forms.CharField(max_length=200, label="Descrição do estágio")
    application_deadline = forms.DateField(
        widget=forms.SelectDateWidget,
        label="Data limite para submissão de candidaturas"
    )
    """
    beggining_date = forms.DateField('Beggining date', required = False)
    duration = forms.IntegerField(choices = Internship.MONTHS_CHOICES)
    working_time = forms.CharField(max_length = 15, choices = Internship.WORK_TIME_CHOICES)
    payment = forms.CharField(max_length = 30)
    location = forms.CharField(max_length = 100)
    n_positions = forms.SmallIntegerField()
    """


class InscriptionAddForm(forms.Form):
    pass