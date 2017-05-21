from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import customer
from .models import products
from .models import bills

def invoice(request):
    customer_table = customer.objects.all()
    products_table = products.objects.all()
    bills_table = bills.objects.all()
    new = next_bill()+1
    context = {
        'customer':customer_table,
        'products':products_table,
        'bills':bills_table,
        'new':new,
    }
    return render(request, 'invoice/billing.html', context)

def next_bill():
    last_record = bills.objects.all().last()
    if not last_record:
        return 0
    else:
        return last_record.id
