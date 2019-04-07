from django.contrib import admin

from .models import Category, Product, Order, Profile, Address, CartItem, Image
from .views import (
    UserCreateAPIView,
    CategorysList,
    ProfileDetailView,
    ProfileUpdateView,
    AddressUpdateView,
    AddressDeleteView,
    AddressCreateView,
    OrderListView,
    OrderDetailView,
    ProductListAPIView,
    ProductDetailAPIView,
    CartItemCreateView,
    CartItemUpdateView
)
# Register your models here.


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Profile)
admin.site.register(Address)
admin.site.register(CartItem)
admin.site.register(Image)
