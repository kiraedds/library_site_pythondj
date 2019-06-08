from django.shortcuts import render
from loans.models import Loan
from django.http import Http404
import datetime


# Create your views here.


def index(request):
    all_loans = Loan.objects.all()
    context = {
        'all_loans': all_loans,
    }
    return render(request, 'loans/index.html', context)


def user_loans(request):
    user = request.user
    all_loans = Loan.objects.all().filter(user=user)
    context = {
        'all_loans': all_loans,
    }
    return render(request, 'loans/index.html', context)


def details(request, loan_id):
    try:
        loan = Loan.objects.get(id=loan_id)
    except Loan.DoesNotExist:
        raise Http404("Book does not exist")
    context = {
        'loan': loan,
    }
    return render(request, 'loans/details.html', context)


def return_book(request, loan_id):
    loan = Loan.objects.get(id=loan_id)
    loan.returned = True
    loan.dateOfReturn = datetime.date.today()
    if loan.dateOfReturn > loan.dateOfPlannedReturn:
        delay = loan.dateOfReturn - loan.dateOfPlannedReturn
        loan.charge = delay.days
    else:
        loan.charge = 0.0
    book = loan.book
    book.numberOfBorrowed -= 1
    book.numberOfAvailable = book.numberOfAll - book.numberOfBorrowed
    book.save()
    loan.save()

    user = request.user
    all_loans = Loan.objects.all().filter(user=user)
    context = {
        'all_loans': all_loans,
    }
    return render(request, 'loans/index.html', context)
