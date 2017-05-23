from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import customer, bills
from .form import CustomerForm, BillsForm

def invoice(request):

    customer_table = customer.objects.all()
    bills_table = bills.objects.all()
    new = next_bill()+1
    invoices = new-1
    context = {
        'customer':customer_table,
        'bills':bills_table,
        'new':new,
        'invoices':invoices,
    }
    if request.method == 'POST':
        skip_or_proceed = request.POST.get("hidden_data")
        item_no = request.POST.get("item_no")
        k = int(item_no)
        items = ["a"]*k
        quantity = ["a"]*k
        price = ["a"]*k
        for i in range(k):
          items[i]=request.POST.get("item-box"+str(i+1))
          quantity[i]=request.POST.get("quantity-box"+str(i+1))
          price[i]=request.POST.get("price-box"+str(i+1))

        if skip_or_proceed =="skip":
            for i in range(k):
                BillsForm = bills.objects.create(phone = "unknown", invoice_no = new, item_no=i, item=items[i], quantity=quantity[i], price=price[i])

        elif skip_or_proceed == "proceed":
            name    = request.POST.get('name-box')
            phone   = request.POST.get('phone-box')
            address = request.POST.get('address-box')
            email   = request.POST.get('email-box')
            pincode = request.POST.get('pin-box')
            CustomerForm = customer.objects.create(name = name, address = address, phone = phone, email = email, pincode = pincode)
            for i in range(k):
                BillsForm = bills.objects.create(phone = phone, invoice_no = new, item_no=i, item=items[i], quantity=quantity[i], price=price[i])
    return render(request, 'invoice/billing.html', context)

def next_bill():
    last_record = bills.objects.all().last()
    if not last_record:
        return 0
    else:
        return last_record.invoice_no
