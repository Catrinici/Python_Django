from django.shortcuts import render, HttpResponse, redirect
import random
import string

# Create your views here.
def index(request):
    try:
        request.session['counter'] += 1
    except:
        request.session['counter'] = 1

    print(request.session['counter'])

    word = ''.join(
        [random.choice(string.ascii_uppercase + string.digits) for n in range(14)])
    context = {
        'word':word
    }

    return render(request, "random_word/index.html",context)
