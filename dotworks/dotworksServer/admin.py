from django.contrib import admin

from .models import Company, Student, Internship

admin.site.register(Company)
admin.site.register(Student)
admin.site.register(Internship)