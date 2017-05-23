from django.contrib import admin
from invoice.models import bills
from invoice.models import customer

admin.site.register(bills)
admin.site.register(customer)
