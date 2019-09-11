from django.shortcuts import render, redirect
from django.contrib import messages
from time import strftime, localtime

# Create your views here.
def index(request):
    if 'words' not in request.session:
        word_list = []
        request.session['words'] = word_list
    context = {
        'word_list': request.session['words']
    }
    return render(request, 'session_words/index.html', context)

    
def add_words(request):
    if not request.POST['word']:
        messages.error(request, 'Please add a word!')
        return redirect('/')
    if request.method == 'POST':
        if 'big_font' in request.POST:
            showbig = 1
        else:
            showbig = 0

        new_word = {
            'word': request.POST['word'],
            'color': request.POST['color'],
            'word_size': showbig,
            'time': strftime("%B %d, %Y %I:%M %p", localtime())
        }
        word_list = request.session['words']
        word_list.append(new_word)
        request.session['words'] = word_list
       

    return redirect('/')


def clear(request):
    request.session.clear()
    return redirect('/')
