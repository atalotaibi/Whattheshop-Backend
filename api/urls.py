from django.urls import path
from .views import (
    UserCreateAPIView,
    CategorysList,

    OrderListView,
    OrderDetailView

    ProductListAPIView,
    ProductDetailAPIView,

)
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('CategorysList/', CategorysList.as_view(), name='CategorysList'),

    path('api/order/list/', OrderListView.as_view(), name='api-order-list'),
    path('api/order/<int:order_id>/detail/', OrderDetailView.as_view(), name='api-order-detail'),

    path('product/list/', ProductListAPIView.as_view(), name='product-list'),
    path('product/detail/<int: product_id>/', ProductDetailAPIView.as_view(), name='product-detail'),

]
