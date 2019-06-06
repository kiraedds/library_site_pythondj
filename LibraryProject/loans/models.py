from django.db import models
from books.models import Book
from django.contrib.auth.models import User


# Create your models here.


class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT, null=False, help_text="Book")
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False, help_text="User who borrowed")
    dateOfLoan = models.DateField(help_text="Date of loan", null=False)
    dateOfPlannedReturn = models.DateField(help_text="Date of planned return", null=False)
    dateOfReturn = models.DateField(help_text="Date of actual return", null=True)
