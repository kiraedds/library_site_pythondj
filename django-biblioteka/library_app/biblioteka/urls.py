from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.book_list, name='book_list'),
    url(r'^(\w{13})$', views.book_detail, name='book_detail')
]
