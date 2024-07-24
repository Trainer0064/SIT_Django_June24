from django.shortcuts import render,HttpResponse
from rest_framework import generics,status,permissions,filters
from .models import TaskModel,TodoModel
from .serializers import TaskModelGenericSerializer,TodoModelGenericSerilizer,TodoModelListSerializer
from .serializers import TaskModelCreateSerializer
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination

# from django.contrib.auth import login,get_user_model
# Create your views here.
# def login_view(request):
#     user = get_user_model().objects.get(id=2)
#     login(request, user)
#     return HttpResponse("Login Successful")

class TaskModelListAPIView(generics.ListAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskModelGenericSerializer
    permission_classes = [permissions.IsAuthenticated,permissions.IsAdminUser]
    filter_backends = [filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend]
    search_fields = ['title','description']
    # TaskModel.objects.filter(title__icontains="Create",description__icontains="Create")
    ordering_fields = ['title','id']
    # TaskModel.objects.order_by('title')
    filterset_fields = ['title',]
    pagination_class = LimitOffsetPagination



class TaskModelCreateAPIView(generics.CreateAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskModelGenericSerializer
    # permission_classes=[permissions.IsAuthenticated]
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


#Customizations in CBV

class CustomizedTaskModelCreateAPIView(generics.CreateAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskModelCreateSerializer

    def create(self, request):
        try:
            serializer = self.serializer_class(data = request.data, context={"request":request})
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"Object created successfully"},status=status.HTTP_201_CREATED)
            else:
                return Response({"message":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message":f"Something went wrong -> {e}"},status=status.HTTP_400_BAD_REQUEST)
        

class CustomizedTaskModelRUDAPIView(generics.GenericAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskModelGenericSerializer

    def get(self,request,id):
        try:
            query = self.queryset.get(id=id)
            serializer =self.serializer_class(query,many=False,context={"request":request})
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":f"Something went wrong -> {e}"},status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request,id):
        try:
            query = self.queryset.get(id=id)
            serializer = TaskModelCreateSerializer(query, data=request.data,context={"request":request})
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"Object updated successfully"},status=status.HTTP_200_OK)
            else:
                return Response({"message":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message":f"Something went wrong -> {e}"},status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request,id):
        try:
            query = self.queryset.get(id=id)
            query.delete()
            return Response({"message":"Object deleted successfully"},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":f"Something went wrong -> {e}"},status=status.HTTP_400_BAD_REQUEST)
        

class TodoModelListAPIView(generics.ListAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoModelListSerializer