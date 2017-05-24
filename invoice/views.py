from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import invoice, items
from .form import InvoiceForm, ItemsForm

def invoice_app(request):

    invoice_table = invoice.objects.all()
    items_table = items.objects.all()
    new = next_bill()+1
    invoices = new-1
    context = {
        'invoice_table':invoice_table,
        'items_table':items_table,
        'new':new,
        'invoices':invoices,
    }

    if request.method == 'POST':
        skip_or_proceed = request.POST.get("hidden_data")
        print(skip_or_proceed)
        tax_percent         = request.POST.get("tax-box")
        discount_percent    = request.POST.get("discount-box")
        sub_total           = request.POST.get("subtotal-box-1")
        tax_amount          = request.POST.get("taxamount-box-1")
        discount_amount     = request.POST.get("discountamount-box-1")
        grand_total         = request.POST.get("grandtotal-box-1")
        item_no = request.POST.get("item_no")
        k = int(item_no)
        item = ["a"]*k
        quantity = ["a"]*k
        price = ["a"]*k
        for i in range(k):
            item[i]=request.POST.get("item-box"+str(i+1))
            quantity[i]=request.POST.get("quantity-box"+str(i+1))
            price[i]=request.POST.get("price-box"+str(i+1))

        for i in range(k):
            ItemsForm = items.objects.create(invoice_no = new, item_no=i, item=item[i], quantity=quantity[i], price=price[i])

        if skip_or_proceed =="skip":
            name    = "unknown"
            phone   = "unknown"
            address = "unknown"
            email   = "unknown"
            pincode = "0"
        elif skip_or_proceed == "proceed":
            name    = request.POST.get("name-box")
            phone   = request.POST.get("phone-box")
            address = request.POST.get("address-box")
            email   = request.POST.get("email-box")
            pincode = request.POST.get("pin-box")
        InvoiceForm = invoice.objects.create(name=name,address=address,phone=phone,email=email,pincode=pincode,invoice_no=new,tax_percent=tax_percent,discount_percent=discount_percent,sub_total=sub_total,tax_amount=tax_amount,discount_amount=discount_amount,grand_total=grand_total )
    return render(request, 'invoice/billing.html', context)

def next_bill():
    last_record = invoice.objects.all().last()
    if not last_record:
        return 0
    else:
        return int(last_record.invoice_no)
