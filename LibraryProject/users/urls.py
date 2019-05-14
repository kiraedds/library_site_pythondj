from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index),
    url(r'^(?P<user_id>[0-9]+)/$', views.details),
    #url(r'^search-form/$', views.search_form),
    #url(r'^search/$', views.search),

    path(r'search-form/',  views.search_form),
    path(r'search/', views.search),
]
