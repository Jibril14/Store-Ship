from django.contrib import admin
from .models import Product, Review, Order, OrderedItem, ShippingAddress
# Register your models here.


admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(OrderedItem)
admin.site.register(ShippingAddress)