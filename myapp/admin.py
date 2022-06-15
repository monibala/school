from django.contrib import admin

from .models import  Checkout, Classes, Order, OrderItem

# Register your models here.
admin.site.register(Classes)
admin.site.register(Order)
admin.site.register(Checkout)
admin.site.register(OrderItem)