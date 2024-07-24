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
    
class TaskModelCreateSerializer(serializers.ModelSerializer):
    # user = serializers.IntegerField(read_only=False)
    class Meta:
        model = TaskModel
        fields = "__all__"
        # exclude = ('description',)

    def validate(self, data):
        print("Data from validation : ",data)
        if "user" in data:
            raise serializers.ValidationError({"user": "This field is required."})
        request = self.context.get('request')
        if request.user.TodoModel_user.first().tasks.all().count() >=5:
            raise serializers.ValidationError({"user": "You have reached the maximum limit of tasks."})
        return data

    def create(self, validated_data):
        print("Validated data from Create : ",validated_data)
        # TaskModel.objects.create(task=validated_data['task'],description=validated_data['description'])
        # print(self.context['request'].data['img_count'])
        task_instance = TaskModel.objects.create(**validated_data)
        user_todo_instance = self.context['request'].user.TodoModel_user.first()
        user_todo_instance.tasks.add(task_instance)
        user_todo_instance.save()
        
        return validated_data
    
    # def update(self, instance, validated_data):
    #     print("Validated data from Update : ",validated_data)
    #     # validated_data.pop('user')
    #     instance.title = validated_data['title']
    #     instance.description = validated_data['description']
    #     instance.save()
    #     user_instance = get_user_model().objects.get(id=validated_data['user'])
    #     user_todo_instance = user_instance.TodoModel_user.first()
    #     user_todo_instance.tasks.add(instance)
    #     user_todo_instance.save()
    #     return validated_data