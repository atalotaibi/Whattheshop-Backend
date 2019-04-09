from django.contrib import admin

from .models import Category, Product, Order, Profile, Address, CartItem, Image

# Register your models here.


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Profile)
admin.site.register(Address)
admin.site.register(CartItem)
admin.site.register(Image)
