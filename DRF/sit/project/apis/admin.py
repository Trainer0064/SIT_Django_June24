from django.contrib import admin
from .models import TaskModel,TodoModel

# Register your models here.
admin.site.register(TaskModel)
admin.site.register(TodoModel)