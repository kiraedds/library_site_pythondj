from django.db import models
from books.models import Book
from django.contrib.auth.models import User


# Create your models here.


class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, help_text="Book")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, help_text="User who borrowed")
    returned = models.BooleanField(default=False, null=False, help_text="Returned or not")
    charge = models.FloatField(default=0.0, null=False, help_text="Charge for not returning the book on time")
    paid = models.BooleanField(default=False, null=False, help_text="Paid or not pain")
    dateOfLoan = models.DateField(help_text="Date of loan", null=False)
    dateOfPlannedReturn = models.DateField(help_text="Date of planned return", null=False)
    dateOfReturn = models.DateField(help_text="Date of actual return", null=True)
