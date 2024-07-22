from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class TaskModel(models.Model):
    title = models.CharField(max_length=100,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    due_data = models.DateField(null=True, blank=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True,editable=False)

    def __str__(self):
        return self.title

class TodoModel(models.Model):
    user = models.ForeignKey(get_user_model(), related_name="TodoModel_user",on_delete=models.CASCADE,null=True,blank=True)
    tasks = models.ManyToManyField(TaskModel,related_name="TodoModel_tasks",blank=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True,editable=False)