# coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField(max_length=100, blank=False)
    e_mail = models.EmailField(blank=False, unique=True)
    description = models.TextField(max_length=500, blank=False)
    website = models.URLField(max_length=100, blank=True)
    facebook = models.URLField(max_length=100, blank=True)

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'."
        + "Up to 15 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=15,
        blank=False
    )

    # Validators should be a list
    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    e_mail = models.EmailField(blank=False, unique=True)
    description = models.TextField(max_length=500, blank=False)
    github = models.URLField(max_length=100, blank=True)
    linkedin = models.URLField(max_length=100, blank=True)
    behance = models.URLField(max_length=100, blank=True)

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'." +
        "Up to 15 digits allowed."
    )

    phone_number = models.CharField(validators=[phone_regex],
        max_length=15,
        blank=False
    )

    # Validators should be a list
    name = models.CharField(max_length=100, blank=False)
    city = models.CharField(max_length=100, blank=False)
    birth_date = models.DateField(blank=False)
    degree = models.CharField(
        max_length=100,
        blank=False
    )

    def __str__(self):
        return self.e_mail


class Internship(models.Model):
    MONTHS_CHOICES = [
        (1, '1 mês'), (2, '2 meses'), (3, '3 meses'), (4, '4 meses'),
        (5, '5 meses'), (6, '6 meses'), (7, '7 meses'), (8, '8 meses'),
        (9, '9 meses'), (10, '10 meses'), (11, '11 meses'), (12, '12 meses')
    ]
    WORK_TIME_CHOICES = [
        ('P_T', 'Part time'), ('F_T', 'Full time'),
    ]
    TYPE_CHOICES = [
        ('CUR', 'Curricular'),
        ('PRO', 'Profissional'),
        ('VER', 'Verao'),
    ]
    PAYMENT_CHOICES = [
        ('R', 'Remunerado'),
        ('NR', ' Não Remunerado'),
    ]

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=TYPE_CHOICES)
    description = models.CharField(max_length=800)
    area = models.CharField(max_length=50)  # JSON list!!!
    beginning_date = models.DateField('Beginning date', blank=True, null=True)
    duration = models.PositiveSmallIntegerField(choices=MONTHS_CHOICES, blank=True, null=True)
    working_time = models.CharField(max_length=15, choices=WORK_TIME_CHOICES, blank=False)
    application_deadline = models.DateField('aplications deadline')
    payment = models.CharField(max_length=30, choices=PAYMENT_CHOICES)
    location = models.CharField(max_length=100)
    n_positions = models.IntegerField()
    avatar = models.CharField(max_length=300)

    def __str__(self):
        return self.company.name + ' ' + self.title


class Inscription(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE)
    answers = ArrayField(
        models.CharField(max_length=1000),
        size=2,
        blank=False
    )


    def __str__(self):
        return self.student.name + ' ' + self.internship.company.name
