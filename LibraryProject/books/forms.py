from django.db import models
from authors.models import Author
from publishers.models import Publisher
from django import forms


class BookForm(forms.Form):
    GENRES = (
        ('FAN', 'Fantasy'),
        ('SF', 'Science Fiction'),
        ('WEST', 'Western'),
        ('ROM', 'Romance'),
        ('THR', 'Thriller'),
        ('MYST', 'Mystery'),
        ('DS', 'Detective Story'),
        ('MEM', 'Memoir'),
        ('BIO', 'Biography'),
        ('PLAY', 'Play'),
        ('MUS', 'Musical'),
        ('SAT', 'Satire'),
        ('HAIKU', 'Haiku'),
        ('HOR', 'Horror'),
        ('DIY', 'DIY'),
        ('DICT', 'Dictionary'),
    )
    title = forms.CharField(label='Book_Title', max_length=100)
    author = forms.ModelChoiceField(queryset=Author.objects.order_by('surname'), label='Author')
    ISBN = forms.CharField(label='ISBN', max_length=17)
    year = forms.IntegerField(label='Year of release', max_value=2050)
    genre = forms.ChoiceField(choices=GENRES)
    publisher = forms.ModelChoiceField(queryset=Publisher.objects.order_by('name'), label='Publisher')
    cover = forms.CharField(label='URL of books\' cover')
    numberOfAvailable = forms.IntegerField(label='Number of books available', max_value=100)
