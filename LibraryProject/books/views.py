from django.http import Http404
from django.shortcuts import render
from .models import Book
from .forms import BookForm
from authors.models import Author
from publishers.models import Publisher


# Create your views here.

def search_form(request):
    return render(request, 'books/search_form.html')


def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'books/search_results.html', {'books': books, 'query': q})
    return render(request, 'books/search_form.html', {'error': error})


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
        raise Http404("Book does not exist")
    context = {
        'book': book,
    }
    return render(request, 'books/details.html', context)


def delete_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")
    book.delete()
    all_books = Book.objects.all()
    context = {
        'all_books': all_books,
    }
    return render(request, 'books/index.html', context)


def edit_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")

    form = BookForm(initial={
        'title': book.title,
        'author': book.author,
        'ISBN': book.ISBN,
        'year': book.year,
        'genre': book.genre,
        'publisher': book.publisher,
        'cover': book.cover,
        'numberOfAvailable': book.numberOfAvailable,
        'numberOfAll': book.numberOfAll,
    })

    context = {
        'form': form,
    }

    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            title = request.POST.get('title', )
            ISBN = request.POST.get('ISBN', )
            genre = request.POST.get('genre', )
            author_id = request.POST.get('author', )
            author = Author.objects.get(id=author_id)
            publisher_id = request.POST.get('publisher', )
            publisher = Publisher.objects.get(id=publisher_id)
            year = request.POST.get('year', )
            numberOfAvailable = request.POST.get('numberOfAvailable', )
            numberOfAll = request.POST.get('numberOfAll', )
            book_obj = Book(title=title, ISBN=ISBN, genre=genre, author=author, publisher=publisher,
                            year=year, numberOfAvailable=numberOfAvailable, numberOfAll=numberOfAll)
            book_obj.save()
            book.delete()
            all_books = Book.objects.all()
            context = {
                'all_books': all_books,
            }
        return render(request, 'books/index.html', context)
    return render(request, 'books/edit_book.html', context)


def create_book(request):
    form = BookForm()
    context = {'form': form}

    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():

            title = request.POST.get('title', )
            ISBN = request.POST.get('ISBN', )
            genre = request.POST.get('genre', )
            author_id = request.POST.get('author', )
            author = Author.objects.get(id=author_id)
            publisher_id = request.POST.get('publisher', )
            publisher = Publisher.objects.get(id=publisher_id)
            year = request.POST.get('year', )
            numberOfAvailable = request.POST.get('numberOfAvailable', )
            numberOfAll = request.POST.get('numberOfAll', )
            book_obj = Book(title=title, ISBN=ISBN, genre=genre, author=author, publisher=publisher,
                            year=year, numberOfAvailable=numberOfAvailable, numberOfAll=numberOfAll)
            book_obj.save()
            all_books = Book.objects.all()
            context = {
                'all_books': all_books,
            }
            return render(request, 'books/index.html', context)
    return render(request, 'books/create_book.html', context)
