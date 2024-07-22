from django.shortcuts import render
from rest_framework import generics
from .models import TaskModel,TodoModel
from .serializers import TaskModelGenericSerializer,TodoModelGenericSerilizer

# Create your views here.

class TaskModelListAPIView(generics.ListAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskModelGenericSerializer

class TaskModelCreateAPIView(generics.CreateAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskModelGenericSerializer

class TaskModelGetAPIView(generics.RetrieveAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskModelGenericSerializer

class TaskModelUpdateAPIView(generics.UpdateAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskModelGenericSerializer

class TaskModelDeleteAPIView(generics.DestroyAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskModelGenericSerializer

class TaskModelGetUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskModelGenericSerializer

class TaskModelListCreateAPIView(generics.ListCreateAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskModelGenericSerializer

class TaskModelGetPutDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskModelGenericSerializer

class TodoModelListCreateAPIView(generics.ListCreateAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoModelGenericSerilizer

class TodoModelGetPutDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoModelGenericSerilizer

