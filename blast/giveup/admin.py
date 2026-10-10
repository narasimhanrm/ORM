from django.contrib import admin
from .models import Customer,CustomerAdmin
admin.site.register(Customer,CustomerAdmin)