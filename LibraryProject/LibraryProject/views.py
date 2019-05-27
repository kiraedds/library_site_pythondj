from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

# Create your views here.


def index( request ):
    context = {

    }
    return render( request, 'LibraryProject/main.html', context )

def login(request):
    return render(request, 'LibraryProject/login.html')

def register(request):
    return render(request, 'LibraryProject/register.html')