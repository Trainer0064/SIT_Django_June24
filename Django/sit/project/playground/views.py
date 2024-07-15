from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .student_data import student_detail

from .models import DepartmentModel,StudentModel,EducationModel
# Create your views here.

def first_api(request):
    return HttpResponse("<h1>Hello, This is our first api using Django Framework</h1>")

def json_api(request):
    data = {
        'name': 'John Doe',
        'age': 30,
        'city': 'New York',
        36:"strength"
    }
    return JsonResponse(data)

def dynamic_api(request, name):
    if name == "SIT":
        name = "Silicon University"
    print(type(name))
    return HttpResponse(f"<h1>Hello, {name}!</h1>")

std_data = {
    1	:	"ADITYESWAR  SAHU",
2	:	"ARPIT  SARANGI",
3	:	"DOLAMANI  MEHER",
4	:	"SANJANA  MOHANTA",
5	:	"AKANKSHA  BARIK",
}

def student_api(request, roll_no):
    if roll_no in std_data:
        return HttpResponse(f"<h1>Hello, {std_data[roll_no]}!</h1>")
    else:
        return HttpResponse("<h1>Student not found.</h1>")

# def student_api2(request, str_data):
#     return HttpResponse(str_data)

def test_html(request,attendance):
    data = {
        'name': 'Silicon',
        'age': 12,
        'city': 'BBSR',
        "strength":36,
        "lst":[
            "ADITYESWAR  SAHU","ARPIT  SARANGI","DOLAMANI  MEHER","SANJANA  MOHANTA","AKANKSHA  BARIK",
        ]
    }
    return render(request, 'index.html',context={"class_data":data,"attendance":attendance})


"""
Portfolio Views
"""

def portfolio_home(request):
    return render(request, 'home.html')

def portfolio_about(request):
    return render(request, 'about.html')

def portfolio_projects(request):
    return render(request, 'projects.html')

def portfolio_skills(request):
    return render(request, 'skills.html')

def portfolio_details(request):
    return render(request, 'details.html',context={"data":student_detail})

def read_all_view(request):
    data = DepartmentModel.objects.all()
    return render(request, 'read_all.html',context={"data":data})

def read_view(request,id):
    data = DepartmentModel.objects.get(id=id)
    return render(request, 'read.html',context={"data":data})

def create_view(request):
    if request.method == 'POST':
        print(request.POST)
        DepartmentModel.objects.create(title=request.POST.get('title'),description=request.POST.get('description'))
        return redirect("read_all")
    return render(request, 'create.html')

def update_view(request,id):
    data = DepartmentModel.objects.get(id=id)
    if request.method == 'POST':
        print(request.POST['title'])
        data.title = request.POST.get('title')
        data.description = request.POST.get('description')
        data.save()
        return redirect('read',id=id)
    return render(request, 'update.html',context={"data":data})


def delete_view(request,id):
    DepartmentModel.objects.get(id=id).delete()
    return redirect('read_all')