from django.urls import path
from .views import (
    UserCreateAPIView,
    CategorysList,
    ProductListAPIView,
    ProductDetailAPIView,
)
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('CategorysList/', CategorysList.as_view(), name='CategorysList'),
    path('product/list/', ProductListAPIView.as_view(), name='product-list'),
    path('product/detail/<int: product_id>/', ProductDetailAPIView.as_view(), name='product-detail'),
]
