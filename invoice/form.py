from django import forms
from django.forms import ModelForm
from invoice.models import invoice, items

class InvoiceForm(forms.ModelForm):
    address = forms.CharField(widget = forms.Textarea)
    class Meta:
        model = invoice
        fields = ['name', 'address', 'phone', 'email', 'pincode', 'invoice_no', 'tax_percent', 'discount_percent', 'sub_total', 'tax_amount', 'discount_amount', 'grand_total']

class ItemsForm(forms.ModelForm):
    class Meta:
        model = items
        fields = ['invoice_no', 'item_no', 'item', 'quantity', 'price']
