from django.contrib import admin
from invoice.models import invoice
from invoice.models import customer
from invoice.models import products
admin.site.register(invoice)
admin.site.register(customer)
admin.site.register(products)
