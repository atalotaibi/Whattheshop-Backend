from django.contrib import admin
from .models import Brand, Product, Order, Profile, Address, Varient, CartItem
# Register your models here.


admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Profile)
admin.site.register(Address)
admin.site.register(Varient)
admin.site.register(CartItem)
