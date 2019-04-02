from django.shortcuts import render, get_object_or_404
from .models import Book


def book_list(request):
    books = Book.objects.all()
    return render(request, 'biblioteka/book/list.html', {'books': books})


def book_detail(request, Isbn):
    book = get_object_or_404(Book, isbn=Isbn)

    return render(request, 'biblioteka/book/detail.html', {'book': book})


# Create your views here.
