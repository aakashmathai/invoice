from django.db import models
from django.utils import timezone

class customer(models.Model):
	name = models.CharField(max_length = 30)
	address = models.CharField(max_length = 200)
	email = models.EmailField(max_length = 50)
    	phone = models.CharField(max_length = 12)
	pincode = models.CharField(max_length = 6)
	date = models.DateTimeField(default=timezone.now)
	
	
class products(models.Model):
	product_name = models.CharField(max_length = 30)
	product_price = models.IntegerField()
	
class invoice(models.Model):
	phone = models.CharField(max_length = 15)
	item_no = models.IntegerField()
	item = models.CharField(max_length = 30)
	quantity = models.IntegerField()
