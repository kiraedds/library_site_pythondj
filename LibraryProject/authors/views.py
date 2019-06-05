from django.shortcuts import render
from django.http import Http404
from authors.models import Author
from authors.forms import AuthorForm


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


def create_author(request):
    form_author = AuthorForm()
    context = {'form_author': form_author}
    if request.method == 'POST':
        form_author = AuthorForm(request.POST)

        if form_author.is_valid():
            name = request.POST.get('name', )
            surname = request.POST.get('surname', )
            birthYear = request.POST.get('birthYear', )
            facePhoto = request.POST.get('facePhoto', )
            author_obj = Author(name=name, surname=surname, birthYear=birthYear, facePhoto=facePhoto)
            author_obj.save()
            all_authors = Author.objects.all()
            context = {
                'all_authors': all_authors,
            }
        return render(request, 'authors/index.html', context)
    return render(request, 'authors/create_author.html', context)
