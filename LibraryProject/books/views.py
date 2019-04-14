from django.http import Http404
from django.shortcuts import render
from .models import Book

# Create your views here.


def index(request):
    all_books = Book.objects.all()
    context = {
        'all_books': all_books,
    }
    return render(request, 'books/index.html', context)


def details(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404("Album does not exist")
    context = {
        'book': book,
    }
    return render(request, 'books/details.html', context)