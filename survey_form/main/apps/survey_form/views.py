from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited


def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['count'] += 1
    return render(request,"survey_form/index.html")



def create(request):
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        return redirect('/result')
    else:
        return redirect('/')
  

def result(request):
    
    return render(request,"survey_form/result.html")

