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
