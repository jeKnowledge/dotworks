# coding=utf-8
import datetime
from django import forms
from django.forms import ModelForm
from .models import Student, Internship, Inscription


class LoginForm(forms.Form):
    username = forms.CharField(
        label='email',
        max_length=100,
        widget=forms.TextInput(attrs={'class': "in"})
    )
    password = forms.CharField(
        label='Palavra-Passe',
        widget=forms.PasswordInput(attrs={'class': "in"})
    )


class StudentRegisterForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Nome Completo',
        required=True,
        widget=forms.TextInput(attrs={'class': "in in2"})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={'class': "in in2"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': "in in2"}),
        label='Introduza a sua password',
        required=True
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': "in in3"}),
        max_length=500,
        label='Um texto sobre si [max:500car]',
        required=True
    )
    github = forms.URLField(
        max_length=100,
        label='Github',
        required=False,
        widget=forms.TextInput(attrs={'class': "in in2"})
    )
    linkedin = forms.URLField(
        max_length=100,
        label='Linkedin',
        required=False,
        widget=forms.TextInput(attrs={'class': "in in2"})
    )
    facebook = forms.URLField(
        max_length=100,
        label='Facebook',
        required=False,
        widget=forms.TextInput(attrs={'class': "in in2"})
    )
    phone = forms.RegexField(
        regex=r'^\+?1?\d{9,15}$',
        max_length=15,
        min_length=9,
        label='Telemovel',
        required=True,
        widget=forms.TextInput(attrs={'class': "in in2"})
    )
    city = forms.CharField(
        max_length=100,
        label='Cidade',
        required=True,
        widget=forms.TextInput(attrs={'class': "in in2"})
    )
    country = forms.CharField(
        max_length=100,
        label='Pais',
        required=True,
        widget=forms.TextInput(attrs={'class': "in in2"})
    )
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': "in in2"}),
        label='Data nascimento',
        required=True,
        initial=datetime.date.today
    )
    degree = forms.ChoiceField(
        choices=Student.DEGREE_CHOICES,
        required=True,
        widget=forms.TextInput(attrs={'class': "in in2"})
    )

    def clean_email(self):
        cleaned_data = self.cleaned_data
        email_ = cleaned_data.get('email')
        if Student.objects.filter(e_mail=email_).exists():
            raise forms.ValidationError('This email already exists')
        return email_


class CompanyRegisterForm(forms.Form):
    company = forms.CharField(
        max_length=100,
        label='Nome da Companhia',
        required=True
    )
    email = forms.EmailField(required=True)
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label='Password',
        required=True
    )
    description = forms.CharField(
        widget=forms.Textarea,
        max_length=500,
        label='Descricao[500car]',
        required=True
    )

    site = forms.URLField(
        max_length=100,
        label='Site da empresa',
        required=True
    )
    facebook = forms.URLField(
        max_length=100,
        label='Facebook',
        required=False
    )
    phone = forms.RegexField(
        regex=r'^\+?1?\d{9,15}$',
        max_length=15,
        min_length=9,
        label="Telemovel",
        required=True
    )


class InternshipCreationForm(forms.Form):
    title = forms.CharField(max_length=100, label='Titulo do estágio')
    description = forms.CharField(max_length=200, label='Descrição do estágio')
    application_deadline = forms.DateField(
        widget=forms.SelectDateWidget,
        label='Data limite para submissão de candidaturas'
    )
    beginning_date = forms.DateField(
        widget=forms.SelectDateWidget,
        label='Beginning Date'
    )
    duration = forms.ChoiceField(choices=Internship.MONTHS_CHOICES, required=True)
    working_time = forms.ChoiceField(choices=Internship.WORK_TIME_CHOICES, required=True)
    payment = forms.CharField(max_length=30)
    location = forms.CharField(max_length=100)
    n_positions = forms.IntegerField(label='Number of Positions')


class InternshipEditForm(forms.ModelForm):
    class Meta:
        model = Internship
        fields = [
            'title',
            'description',
            'beginning_date',
            'duration',
            'working_time',
            'application_deadline',
            'payment',
            'location',
            'n_positions'
        ]


class InscriptionAddForm(forms.Form):
    first_question = 'What do you do in your free time?'
    second_question = 'Why are you applying?'
    first_answer = forms.CharField(max_length=500, label=first_question)
    second_answer = forms.CharField(max_length=500, label=second_question)


class ChangePasswordForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label='Current password',
        required=True
    )
    new_password = forms.CharField(
        widget=forms.PasswordInput(),
        label='New password',
        required=True
    )
    confirm_new_password = forms.CharField(
        widget=forms.PasswordInput(),
        label='Confirm new password',
        required=True
    )
