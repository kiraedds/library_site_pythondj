from django.db import models
from authors.models import Author
from publishers.models import Publisher

# Create your models here.


class Book(models.Model):

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

    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    ISBN = models.CharField(max_length=13)
    genre = models.CharField(max_length=20, choices=GENRES, blank=True, default='Undefined',
                             help_text="Genre of the book")
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True)
    cover = models.CharField(max_length=300)

    def __str__(self):
        return str(self.title) + ' - ' + str(self.author)