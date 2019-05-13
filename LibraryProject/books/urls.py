from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index),
    url(r'^(?P<book_id>[0-9]+)/$', views.details),
    #url(r'^(?P<create_book>[w]+', views.create_book),
    path(r'create_book/',  views.create_book),
    path(r'search-form/',  views.search_form),
    path(r'search/', views.search),
]
