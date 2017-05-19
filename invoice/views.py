from django.shortcuts import render
from django.utils import timezone
from .models import customer
from .models import products
from .models import invoice

def invoice(request):
    	return render(request, 'invoice/billing.html', {})

