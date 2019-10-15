from django.shortcuts import render,redirect
from .models import UserManager,User
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,'login_app/index.html')

def register(request):
    if request.method == "POST":
        print request.POST
        response_from_models = User.objects.add_user(request.POST)
        # if failed validations
        if response_from_models['status'] == False:
            for error in response_from_models['errors']:
                messages.error(request, error)
            return redirect('users:index')
            #if true on validations
        else:
            request.session['user_id'] = response_from_models['user'].id
            print response_from_models['user']
            return redirect('users:succes')
    else:
        return redirect('users:succes')

def login(request):
    print request.POST
    response_from_models = User.objects.check_user(request.POST)
    print response_from_models
    if not response_from_models['status']:
        for error in response_from_models['errors']:
            messages.error(request, error)
        return redirect('users:index')
    else:
        request.session['user_id'] = response_from_models['user_id']

    return redirect('users:succes')


def succes(request):
    if not 'user_id' in request.session:
        messages.error(request, "Must be logged in!")
        return redirect('users:index')

    return render(request,'login_app/succes.html')

def logout(request):
    request.session.clear()
    return redirect('users:index')
