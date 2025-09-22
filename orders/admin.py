from django.contrib import admin

# Register your models here.
from .models import Order, OrderStatus

admin.site.register(Order)
admin.site.register(OrderStatus)