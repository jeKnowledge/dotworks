# coding=utf-8
import datetime
from django import forms
from django.forms import ModelForm
from dotworks_server.models import Student, Internship, Inscription
from django.utils.translation import gettext_lazy as _


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Email',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'in'})
    )
    password = forms.CharField(
        label='Palavra-Passe',
        widget=forms.PasswordInput(attrs={'class': 'in'})
    )


class StudentRegisterForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Nome Completo',
        required=True,
        widget=forms.TextInput(attrs={'class': 'in in2'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'in in2'}),
        error_messages={'invalid': 'Email inválido'}
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'in in2'}),
        label='Palavra-Passe',
        min_length=4,
        required=True
    )
    github = forms.URLField(
        max_length=100,
        label='Github',
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Opcional',
                'class': 'in in2 not-required',
            }
        ),
        error_messages={'invalid': 'Github inválido'}
    )
    linkedin = forms.URLField(
        max_length=100,
        label='Linkedin',
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Opcional',
                'class': 'in in2 not-required'
            }
        ),
        error_messages={'invalid': 'Linkedin inválido'}
    )
    behance = forms.URLField(
        max_length=100,
        label='Behance',
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Opcional',
                'class': 'in in2 not-required'
            }
        ),
        error_messages={'invalid': 'Behance inválido'}
    )
    phone = forms.RegexField(
        regex=r'^\+?1?\d{9,15}$',
        max_length=15,
        min_length=9,
        label='Telemóvel',
        required=True,
        widget=forms.TextInput(attrs={'class': 'in in2'}),
        error_messages={'invalid': 'Número de telemóvel inválido'}
    )
    city = forms.CharField(
        max_length=100,
        label='Localidade',
        required=True,
        widget=forms.TextInput(attrs={'class': 'in in2'})
    )
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'in in2'}),
        label='Data de nascimento',
        required=True,
        initial=datetime.date.today,
        error_messages={'invalid': 'Data inválida'}
    )
    degree = forms.CharField(
        required=True,
        label='Curso',
        widget=forms.TextInput(attrs={'class': 'in in2'})
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'in in3'}),
        max_length=500,
        label='Um texto sobre ti',
        required=True
    )
    terms_and_conditions = forms.BooleanField(label='Aceito os termos e condições')

    def clean_email(self):
        cleaned_data = self.cleaned_data
        email_ = cleaned_data.get('email')
        if Student.objects.filter(e_mail=email_).exists():
            raise forms.ValidationError('Este email já existe')
        return email_


class StudentEditProfile(forms.ModelForm):
    e_mail = forms.EmailField(error_messages={'unique': 'Este email já existe'})
    class Meta:
        model = Student
        fields = (
            'name',
            'e_mail',
            'github',
            'linkedin',
            'behance',
            'phone_number',
            'city',
            'birth_date',
            'degree',
            'description'
        )
        labels = {
            'name': _('Nome'),
            'e_mail': _('Email'),
            'phone_number': _('Número de Telemóvel'),
            'city': _('Cidade'),
            'birth_date': _('Data de Nascimento'),
            'degree': _('Curso'),
            'description': _('Descrição')
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'in in2'})


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
    payment = forms.ChoiceField(choices=Internship.PAYMENT_CHOICES)
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
    first_question = 'Competências Técnicas'
    second_question = 'Competências Pessoais Relevantes'
    first_answer = forms.CharField(
        max_length=1000,
        label=first_question,
        widget=forms.Textarea(attrs={'placeholder': 'ex: C++, javascript, html, photoshop', 'class': 'in'})
    )
    second_answer = forms.CharField(
        max_length=1000,
        label=second_question,
        widget=forms.Textarea(attrs={'placeholder': 'ex: criatividade, organização', 'class': 'in'})
    )


class ChangePasswordForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': "in in2"}),
        label='Password Atual',
        required=True
    )
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': "in in2"}),
        label='Nova Password',
        min_length=4,
        required=True
    )
    confirm_new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': "in in2"}),
        label='Confirmar Nova Password',
        min_length=4,
        required=True
    )
