from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(primary_key=True, max_length=200, help_text='gatunek)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    objects = models.Manager()


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField(primary_key=True, max_length=13)
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('biblioteka:book_detail', args=[self.isbn])

    objects = models.Manager()


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']
        unique_together = ("first_name", "last_name", "date_of_birth")

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

    objects = models.Manager()


import uuid


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} ({self.book.title})'

    objects = models.Manager()