from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index),
    url(r'^(?P<book_id>[0-9]+)/$', views.details),
    # url(r'^(?P<create_book>[w]+', views.create_book),
    path(r'create_book/', views.create_book),
    path('delete_book/<book_id>', views.delete_book),
    url(r'^edit_book/(?P<book_id>[0-9]+)/$', views.edit_book),
    url(r'^reserve_book/(?P<book_id>[0-9]+)/$', views.borrow_book),
    path('authors_books/<author_id>', views.authors_books),
    path('publishers_books/<publisher_id>', views.publishers_books),
    path(r'search-form/', views.search_form),
    path(r'search/', views.search),
]
