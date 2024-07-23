from rest_framework import serializers
from .models import TaskModel,TodoModel
from django.contrib.auth import get_user_model

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

class TaskModelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = "__all__"

class UserModelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        # fields = "__all__"
        exclude = ('password','groups','user_permissions')

class TodoModelListSerializer(serializers.ModelSerializer):
    user_details = serializers.SerializerMethodField(read_only=True)
    task_details = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = TodoModel
        fields = "__all__"

    def get_user_details(self, obj):
        try:
            data = UserModelListSerializer(obj.user,many=False).data
        except Exception as e:
            print(e)
            data = None
        return data

    def get_task_details(self, obj):
        try:
            data = TaskModelListSerializer(obj.tasks.all(),many=True).data
        except Exception as e:
            print(e)
            data = None
        return data
    
