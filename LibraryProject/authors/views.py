from django.shortcuts import render
from django.http import Http404
from .models import Author

# Create your views here.


def index(request):
    all_authors = Author.objects.all()
    context = {
        'all_authors': all_authors,
    }
    return render(request, 'authors/index.html', context)


def details(request, author_id):
    try:
        author = Author.objects.get(id=author_id)
    except Author.DoesNotExist:
        raise Http404("Author does not exist")
    context = {
        'author': author,
    }
    return render(request, 'authors/details.html', context)
