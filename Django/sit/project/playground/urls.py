from django.urls import path
from .views import first_api,json_api

urlpatterns = [
    path('first-api/',first_api,name='first-api'),
    path('json-api/',json_api,name='json-api'),
]