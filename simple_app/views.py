from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from .models import Transaction

import os
import requests
from django.conf import settings

# Create your views here.
class TransactionListView(ListView):
    model = Transaction
    template_name = 'index.html'
    context_object_name = 'transaction_list'

class TransactionDetailView(DetailView):
    model = Transaction
    template_name = "detail.html"

def add(request):
    cc_num = request.POST['CCNum']
    exp_date = request.POST['ExpDate']
    cvc_num = request.POST['CVCNum']
    transaction = Transaction(cc_num=cc_num, exp_date=exp_date, cvc_num=cvc_num)
    transaction.save()
    return HttpResponseRedirect("/" + str(transaction.id) + "/")

def reveal(request):
    vgs_outbound_route = getattr(settings, "OUTBOUND_ROUTE", None)

    if vgs_outbound_route is not None:
        os.environ['HTTPS_PROXY'] = vgs_outbound_route
        os.environ['REQUESTS_CA_BUNDLE'] = os.getcwd() + '/cert.pem'
    
    response = requests.post('https://echo.apps.verygood.systems/post',json=request.POST).json()

    context = {
        'CCNum': response['json']['CCNum'],
        'ExpDate': response['json']['ExpDate'],
        'CVCNum': response['json']['CVCNum'],
    }

    return render(request, 'reveal.html', context)

