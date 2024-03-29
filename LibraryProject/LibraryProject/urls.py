"""
LibraryProject URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('history/', include('history.urls')),
    path('users/', include('users.urls')),
    path('authors/', include('authors.urls')),
    path('publishers/', include('publishers.urls')),
    path('loans/', include('loans.urls')),
    path(r'login/', views.login),
    path(r'register/', views.register),
    path('menu/', include('menu.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
