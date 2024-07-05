from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.

def first_api(request):
    return HttpResponse("Hello, This is our first api using Django Framework")

def json_api(request):
    data = {
        'name': 'John Doe',
        'age': 30,
        'city': 'New York'
    }
    return JsonResponse(data)