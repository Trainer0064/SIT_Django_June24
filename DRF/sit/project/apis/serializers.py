from rest_framework import serializers
from .models import TaskModel,TodoModel

class TaskModelGenericSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = "__all__"
        # fields = ('id','title')
        # exclude = ('id',)

class TodoModelGenericSerilizer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = "__all__"