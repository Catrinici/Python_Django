from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
    courses = Course.objects.all()
    context = {
        "daniel": courses
    }
    return render(request,"courses_app/index.html", context)

def addCourse(request):
    Course.objects.create(name=request.POST['name'],description=request.POST['description'])
    return redirect('/')

def destroy(request, id):
    context = {
     "course":Course.objects.get(id=id)
    }
    return render(request, 'courses_app/destroy.html',context)

def confirmDestroy(request, id):
    deleteMe = Course.objects.get(id=id)
    deleteMe.delete()
    return redirect('/')
