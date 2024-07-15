from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import CourseModel
# Create your views here.
def http_api(request):
    return HttpResponse("<h1>Django Recap</h1>")

def dynamic_api(request,name):
    return HttpResponse(f"<h1>Hello, {name}!</h1>")

def html_api(request):
    return render(request,"base.html")

def read_all_views(request):
    data = CourseModel.objects.all()
    return render(request,"course_list.html",{"data":data})

def create_view(request):
    if request.method == "POST":
        course = CourseModel.objects.create(title=request.POST.get("title"),description=request.POST.get("description"))
        return redirect("read_all_views")

    return render(request,"create_course.html")

def update_view(request,id):
    data = CourseModel.objects.get(id=id)
    if request.method == "POST":   
        data.title = request.POST.get('title')
        data.description = request.POST.get('description')
        data.save()
        return redirect("read_all_views")
    return render(request,"update.html",context={"data":data})

def delete_view(request,id):
    CourseModel.objects.get(id=id).delete()
    return redirect("read_all_views")