from django.http import Http404
from django.shortcuts import render
from publishers.models import Publisher
from publishers.forms import PublisherForm


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


def create_publisher(request):
    form_publisher = PublisherForm()
    context = {'form_publisher': form_publisher}

    if request.method == 'POST':
        form_publisher = PublisherForm(request.POST)

        if form_publisher.is_valid():
            name = request.POST.get('name', )
            publisher_object = Publisher(name=name)
            publisher_object.save()
            all_publishers = Publisher.objects.all()
            context = {
                'all_publishers': all_publishers,
            }
        return render(request, 'publishers/index.html', context)
    return render(request, 'publishers/create_publisher.html', context)
