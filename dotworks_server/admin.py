from django.contrib import admin

from .models import Company, Student, Internship, Inscription


class StudentModelAdmin(admin.ModelAdmin):
    list_filter = ('degree', 'city', 'birth_date')


class InternshipModelAdmin(admin.ModelAdmin):
    list_filter = ('payment', 'duration', 'n_positions')


admin.site.register(Company)
admin.site.register(Student, StudentModelAdmin)
admin.site.register(Internship, InternshipModelAdmin)
admin.site.register(Inscription)
