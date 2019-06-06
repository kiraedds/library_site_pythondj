from django.shortcuts import render
from loans.models import Loan
from django.http import Http404


# Create your views here.

def index(request):
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
