from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def new(request):
    return HttpResponse('placeholder to display a new form to create a new blog, part deux')

def create(request):
    return redirect('/')

def show(request,num):
    # number=num
    # return HttpResponse('placeholder to display blog number'+" "+number)
    number={
        'blog_number':num
    }
    return render(request, 'test.html', number)

def edit(request,num):
    number=num
    return HttpResponse('placeholder to edit blog'+" "+number)

def destroy(request,num):
    return redirect('/')




