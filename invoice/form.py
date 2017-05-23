from django import forms
from django.forms import ModelForm
from invoice.models import customer, bills

class CustomerForm(forms.ModelForm):
    address = forms.CharField(widget = forms.Textarea)
    class Meta:
        model = customer
        fields = ['name', 'address', 'phone', 'email', 'pincode']

class BillsForm(forms.ModelForm):
    class Meta:
        model = bills
        fields = ['phone', 'invoice_no', 'item_no', 'item', 'quantity', 'price']
