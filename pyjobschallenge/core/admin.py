from django.contrib import admin
from .models import Student, StudentApproved, StudentSchoolSubject, SchoolSubject


admin.site.register(Student)
admin.site.register(StudentApproved)
admin.site.register(StudentSchoolSubject)
admin.site.register(SchoolSubject)
