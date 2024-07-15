from django.db import models

# Create your models here.
class DepartmentModel(models.Model):
    title = models.CharField(max_length=50,null=True, blank=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True,editable=False)

    def __str__(self):
        return self.title

class RegistrationModel(models.Model):
    regd_no = models.CharField(max_length=10,null=True, blank=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.regd_no

class CourseModel(models.Model):
    title = models.CharField(max_length=50,null=True,blank=True)
    description = models.TextField(blank=True,null=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.title

class StudentModel(models.Model):
    regd = models.OneToOneField(RegistrationModel,on_delete=models.CASCADE,related_name="StudentModel_regd",null=True,blank=True)
    name = models.CharField(max_length=50,null=True, blank=True)
    dept = models.ForeignKey(DepartmentModel,on_delete=models.SET_NULL,related_name="StudentModel_dept",null=True,blank=True)
    courses = models.ManyToManyField(CourseModel,related_name="StudentModel_courses",blank=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f"{self.name} -> {self.regd.regd_no}"