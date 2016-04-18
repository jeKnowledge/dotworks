from django.contrib import admin

from .models import Company, Student, Internship, Inscription

admin.site.register(Company)
admin.site.register(Student)
admin.site.register(Internship)
admin.site.register(Inscription)