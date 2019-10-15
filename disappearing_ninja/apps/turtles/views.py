from django.shortcuts import render, HttpResponse

def index(request):
    context = {
        'text': "No Ninjas here"
    }
    return render(request, 'turtles/index.html', context)


def ninjas(request):
    context = {
        'text': "All the Ninjas",
        'color': "tmnt.png"
    }
    return render(request, 'turtles/index.html', context)


def show(request, color):

    data = {
        'orange': 'michelangelo.jpg',
        'red': 'raphael.jpg',
        'purple': 'donatello.jpg',
        'blue': 'leonardo.jpg'
    }
    if color not in data:
        context = {
            'text':   "Who are you looking for?",
            'color': 'notapril.jpg'
        }
    else:
        context = {
            'color': data[color],
            'text': color
        }
    return render(request, 'turtles/index.html', context)
