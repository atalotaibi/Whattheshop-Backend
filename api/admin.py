from django.contrib import admin

from .models import Category, Product, Order, Profile, Address, CartItem
# Register your models here.


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Profile)
admin.site.register(Address)
admin.site.register(CartItem)
