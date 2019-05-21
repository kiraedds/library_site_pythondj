from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index),
    url(r'^(?P<author_id>[0-9]+)/$', views.details),
    path(r'create_author/', views.create_author),
]
