from django.db import models

# Create your models here.
class AllFieldsModel(models.Model):
    char_field = models.CharField(max_length=10)
    text_field = models.TextField()
    integer_field = models.IntegerField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    boolean_field = models.BooleanField()
    email_field = models.EmailField()
    url_field = models.URLField()
    date_field = models.DateField()
    datetime_field = models.DateTimeField(auto_now=True)

class DepartmentModel(models.Model):
    title = models.CharField(max_length=50,null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        try:
            return self.title
        except:
            return "NULL"

class RegistrationModel(models.Model):
    regd_no = models.CharField(max_length=20,null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.regd_no

class EducationModel(models.Model):
    title = models.CharField(max_length=50,null=True, blank=True)
    batch_start = models.IntegerField(null=True, blank=True)
    batch_end = models.IntegerField(null=True, blank=True)
    percentile = models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} -> {self.percentile}"

class StudentModel(models.Model):
    name = models.CharField(max_length=50,null=True, blank=True)
    dept = models.ForeignKey(DepartmentModel,on_delete=models.SET_NULL, related_name="StudentModel_dept",null=True)
    regd = models.OneToOneField(RegistrationModel,on_delete=models.CASCADE,related_name="StudentModel_regd",null=True)
    education = models.ManyToManyField(EducationModel,related_name="StudentModel_education")
    
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        try:
            return f"{self.name} -> {self.dept.title}"
        except:
            return f"{self.name} -> NULL"