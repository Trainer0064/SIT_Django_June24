from django.urls import path
from .views import TaskModelListAPIView,TaskModelCreateAPIView,TaskModelGetAPIView,TaskModelUpdateAPIView,TaskModelDeleteAPIView
from .views import TaskModelGetUpdateAPIView,TaskModelListCreateAPIView,TaskModelGetPutDeleteAPIView
from .views import TodoModelListCreateAPIView,TodoModelGetPutDeleteAPIView

from .views import CustomizedTaskModelCreateAPIView,CustomizedTaskModelRUDAPIView,TodoModelListAPIView
# from .views import login_view,test_length

urlpatterns = [
    path('task-list-api/',TaskModelListAPIView.as_view(),name="TaskModelListAPIView"),
    path('task-create-api/',TaskModelCreateAPIView.as_view(),name="TaskModelCreateAPIView"),
    path('task-get-api/<pk>/',TaskModelGetAPIView.as_view(),name="TaskModelGetAPIView"),
    path('task-update-api/<pk>/',TaskModelUpdateAPIView.as_view(),name="TaskModelUpdateAPIView"),
    path('task-delete-api/<pk>/',TaskModelDeleteAPIView.as_view(), name="TaskModelDeleteAPIView"),
    path('task-get-update-api/<pk>/',TaskModelGetUpdateAPIView.as_view(),name="TaskModelGetUpdateAPIView"),
    path('task-list-create-api/',TaskModelListCreateAPIView.as_view(),name="TaskModelListCreateAPIView"),
    path('task-rud-api/<pk>/',TaskModelGetPutDeleteAPIView.as_view(),name="TaskModelGetPutDeleteAPIView"),

    path('todo-list-create-api/',TodoModelListCreateAPIView.as_view(),name="TodoModelListCreateAPIView"),
    path('todo-rud-api/<pk>/',TodoModelGetPutDeleteAPIView.as_view(),name="TodoModelGetPutDeleteAPIView"),
    
    #URLs for Customized CBVs
    path('c-task-create-api/',CustomizedTaskModelCreateAPIView.as_view(),name="CustomizedTaskModelCreateAPIView"),
    path('c-task-rud-api/<id>/',CustomizedTaskModelRUDAPIView.as_view(),name="CustomizedTaskModelRUDAPIView"),

    path('c-todo-list-api/',TodoModelListAPIView.as_view(),name="TodoModelListAPIView"),
    # path('login-api/',login_view,name= 'login_view'),
    # path('test-pswd/<password>/',test_length,name= 'test_length'),

]