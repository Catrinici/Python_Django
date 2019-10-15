from django.shortcuts import render,redirect
from .models import Email

# Create your views here.
def index(request):
    if request.method=='GET':
        return render(request,'index.html')
    elif request.method=="POST":
        result=Email.validate.validate(request.POST['email'])
        print result
        if result ==False:
            context={
                'error':'Invalid Email Address!'
            }
            return render(request,'index.html',context)
        elif result=='dup':
            context={
                'error':'Email Address has existed'
            }
            return render(request,'index.html',context)
        elif result=='error':
            context={
                'error':'Add error'
            }
            return render(request,'index.html',context)
        else:
            request.session['email']=request.POST['email']
            return redirect('/success')

def success(request):
    if request.method=='GET':
        if 'email' not in request.session:
            subemail='nothing'
        else:
            subemail=request.session['email']
            del request.session['email']
        allemails=Email.objects.all()
        context={
            'all_emails':allemails,
            'submitemail':subemail
        }
        return render(request,'success.html',context)
    elif request.method=="POST":
        print request.POST
        if 'id' not in request.POST:
            context={
                'error':'you do not select any!'
            }
            return render(request,'success.html',context)
        else:
            email=Email.objects.get(id=request.POST['id'])
            email.delete()
            allemails=Email.objects.all()
            context={
                'all_emails':allemails,
                'error':'delete successfully!'
            }
            if 'error' in context:
                print context['error']
            return render(request,'success.html',context)
