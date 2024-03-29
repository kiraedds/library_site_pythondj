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

    title = models.CharField(max_length=100, help_text="Title of the book")
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, help_text="Author of the book")
    ISBN = models.CharField(max_length=17,
                            help_text="ISBN of the book, format: xx-xxxxx-xx-x OR yyy-yy-yyyy-yyy-y")
    year = models.PositiveSmallIntegerField(help_text="Year of book release")
    genre = models.CharField(max_length=20, choices=GENRES, default='Undefined',
                             help_text="Genre of the book")
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True, help_text="Publisher of the book")
    cover = models.CharField(max_length=300, help_text="URL of books' cover image", null=True)
    numberOfAll = models.PositiveSmallIntegerField(help_text="Number of all books")
    numberOfBorrowed = models.PositiveSmallIntegerField(help_text="Number of borrowed books.")
    numberOfAvailable = models.PositiveSmallIntegerField(help_text="Number of available books")

    def __str__(self):
        return str(self.title) + ' - ' + str(self.author)
