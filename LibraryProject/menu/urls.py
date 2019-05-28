from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path(r'opening_hours', views.opening_hours),
    path(r'regulamin', views.regulamin),
    path(r'how_to_use_our_library', views.how_to_use_our_library),
    path(r'faq', views.faq),
    path(r'ask', views.ask),
    path(r'contact', views.contact),
    path(r'history', views.history),
]