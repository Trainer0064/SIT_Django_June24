from django.contrib import admin
from .models import DepartmentModel,RegistrationModel,CourseModel,StudentModel
# Register your models here.

admin.site.register(DepartmentModel)
admin.site.register(RegistrationModel)
admin.site.register(CourseModel)
admin.site.register(StudentModel)