from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    context = {
    }
    return render( request, 'menu/main.html', context )


def opening_hours(request):
    return render(request, 'menu/opening_hours.html')


def regulamin(request):
    return render(request, 'menu/regulamin.html')


def how_to_use_our_library(request):
    return render(request, 'menu/how_to_use_our_library.html')


def faq(request):
    return render(request, 'menu/faq.html')


def ask(request):
    return render(request, 'menu/ask.html')


def contact(request):
    return render(request, 'menu/contact.html')


def history(request):
    return render(request, 'menu/history.html')

