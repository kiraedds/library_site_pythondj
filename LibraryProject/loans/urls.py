from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index),
    url(r'^(?P<loan_id>[0-9]+)/$', views.details),
    path('return_book/<loan_id>', views.return_book),
]
