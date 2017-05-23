from django.db import models
from django.utils import timezone

class customer(models.Model):
	name = models.CharField(max_length = 30)
	address = models.CharField(max_length = 200)
	phone = models.CharField(max_length = 12)
	email = models.EmailField(max_length = 50)
	pincode = models.CharField(max_length = 6)
	date = models.DateTimeField(default=timezone.now)

class bills(models.Model):
	phone = models.CharField(max_length = 15)
	invoice_no = models.IntegerField()
	item_no = models.IntegerField()
	item = models.CharField(max_length = 30)
	quantity = models.IntegerField()
	price = models.IntegerField(default = 0)
