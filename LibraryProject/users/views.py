from django.shortcuts import render
from django.http import Http404
from .models import User

# Create your views here.

def search_form(request):
    return render(request, 'users/search_form.html')

def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            users = User.objects.filter(username__icontains=q)
            return render(request, 'users/search_results.html', {'users': users, 'query': q})
    return render(request, 'users/search_form.html', {'error': error})

def index(request):
    all_users = User.objects.all()
    context = {
        'all_users': all_users,
    }
    return render(request, 'users/index.html', context)


def details(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    context = {
        'user': user,
    }
    return render(request, 'users/details.html', context)
