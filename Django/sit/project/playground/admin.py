from django.contrib import admin
from .models import AllFieldsModel,DepartmentModel,StudentModel,RegistrationModel,EducationModel
# Register your models here.
admin.site.register(AllFieldsModel)
admin.site.register(DepartmentModel)
admin.site.register(StudentModel)
admin.site.register(RegistrationModel)
admin.site.register(EducationModel)