from django.contrib import admin
from django.contrib.auth.models import User

from .models import Company, Student, Internship, Inscription


class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'e_mail', 'phone_number', 'degree']
    list_filter = ('degree', 'city', 'birth_date')


class InternshipModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'category', 'payment', 'n_positions', 'duration']
    list_filter = ('payment', 'duration', 'n_positions')


admin.site.register(Company)
admin.site.register(Student, StudentModelAdmin)
admin.site.register(Internship, InternshipModelAdmin)
admin.site.register(Inscription)
