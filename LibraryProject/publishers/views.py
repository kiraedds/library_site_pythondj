from django.http import Http404
from django.shortcuts import render
from .models import Publisher

# Create your views here.


def index(request):
    all_publishers = Publisher.objects.all()
    context = {
        'all_publishers': all_publishers,
    }
    return render(request, 'publishers/index.html', context)


def details(request, publisher_id):
    try:
        publisher = Publisher.objects.get(id=publisher_id)
    except Publisher.DoesNotExist:
        raise Http404("Publisher does not exist")
    context = {
        'publisher': publisher,
    }
    return render(request, 'publishers/details.html', context)
