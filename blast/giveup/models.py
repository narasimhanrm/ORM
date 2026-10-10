from django.db import models
from django.contrib import admin

class Customer(models.Model):
    customer_name = models.CharField(max_length=20)
    customer_phno = models.CharField(max_length=10)
    customer_address = models.TextField()
    customer_mail = models.EmailField()
    delivery_id = models.CharField(max_length=8, primary_key=True)
    delivery_amount = models.FloatField()
    delivery_details = models.TextField()

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'customer_phno', 'customer_address', 'customer_mail', 'delivery_id', 'delivery_amount', 'delivery_details']
