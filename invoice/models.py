from django.db import models
from django.utils import timezone

class invoice(models.Model):
	name = models.CharField(max_length = 30)
	address = models.CharField(max_length = 200)
	phone = models.CharField(max_length = 12)
	email = models.EmailField(max_length = 50)
	pincode = models.CharField(max_length = 6)
	date = models.DateTimeField(default=timezone.now)
	invoice_no = models.CharField(max_length = 100)
	tax_percent = models.CharField(max_length = 100)
	discount_percent = models.CharField(max_length = 100)
	sub_total = models.CharField(max_length = 100)
	tax_amount = models.CharField(max_length = 100)
	discount_amount = models.CharField(max_length = 100)
	grand_total = models.CharField(max_length = 100)

class items(models.Model):
	invoice_no = models.IntegerField()
	item_no = models.IntegerField()
	item = models.CharField(max_length = 300)
	quantity = models.IntegerField()
	price = models.IntegerField()
