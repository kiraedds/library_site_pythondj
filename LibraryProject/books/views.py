from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponseRedirect

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

from .models import Book
from .forms import BookForm
from authors.models import Author
from authors.forms import AuthorForm
from publishers.models import Publisher
from publishers.forms import PublisherForm
def create_book(request):
    form = BookForm()
    form_author = AuthorForm()
    form_publisher = PublisherForm()
    context = {'form': form, 'form_author': form_author, 'form_publisher': form_publisher}

    if request.method=='POST':
        form=BookForm(request.POST)
        form_author=AuthorForm(request.POST)
        form_publisher=PublisherForm(request.POST)


        if form.is_valid():
            title = request.POST.get('title',)
            ISBN = request.POST.get('ISBN',)
            genre = request.POST.get('ISBN',)
            author_id=request.POST.get('author',)
            author=Author.objects.get(id=author_id)
            publisher_id=request.POST.get('publisher',)
            publisher=Publisher.objects.get(id=publisher_id)
            book_obj=Book(title=title, ISBN=ISBN, genre=genre, author=author, publisher=publisher)
            book_obj.save()
            all_books = Book.objects.all()
            context = {
                'all_books': all_books,
            }
            return render(request, 'books/index.html', context)

        if form_author.is_valid():
            name=request.POST.get('name',)
            surname=request.POST.get('surname')
            author_object=Author(name=name,surname=surname)
            author_object.save()

        if form_publisher.is_valid():
            name = request.POST.get('name', )
            publisher_object = Publisher(name=name)
            publisher_object .save()

    return render(request, 'books/create_book.html',context)
