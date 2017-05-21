from django.contrib import admin
from invoice.models import bills
from invoice.models import customer
from invoice.models import products
admin.site.register(bills)
admin.site.register(customer)
admin.site.register(products)
