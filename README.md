# Ex02 Django ORM Web Application
## Date:  09.10.2026

## AIM
To develop a Django Application to store and retrieve data from a Delivery Service Database platform using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
```
models.py
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

admin.py
from django.contrib import admin
from .models import Customer,CustomerAdmin
admin.site.register(Customer,CustomerAdmin)

```


## OUTPUT
![alt text](<Screenshot 2026-10-09 214034.png>)


## RESULT
Thus the program for creating Online Food Delivery Database using ORM hass been executed successfully
