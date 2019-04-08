from django.urls import path
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
    CartItemUpdateView,
    CartItemDeleteView,
    OrderCreateView
)
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('CategorysList/', CategorysList.as_view(), name='CategorysList'),

    path('<int:profile_id>/detail/',
         ProfileDetailView.as_view(), name='api-detail'),
    path('<int:profile_id>/update/',
         ProfileUpdateView.as_view(), name='api-update'),

    path('<int:address_id>/addessUpdate/',
         AddressUpdateView.as_view(), name='addess-update'),
    path('<int:address_id>/addessDelete/',
         AddressDeleteView.as_view(), name='addess-delete'),
    path('addessCreate/',
         AddressCreateView.as_view(), name='addess-create'),

    path('order/create/', OrderCreateView.as_view(), name='api-order-create'),
    path('order/list/', OrderListView.as_view(), name='api-order-list'),
    path('order/<int:order_id>/detail/',
         OrderDetailView.as_view(), name='api-order-detail'),

    path('product/list/', ProductListAPIView.as_view(), name='product-list'),
    path('<int:product_id>/product/detail/',
         ProductDetailAPIView.as_view(), name='product-detail'),
    path('CartItemCreateView/',
         CartItemCreateView.as_view(), name='cartitem-create'),
    path('<int:cartItem_id>/CartItemUpdateView/',
         CartItemUpdateView.as_view(), name='cartitem-update'),
    path('<int:cartItem_id>/CartItemDeleteView/',
         CartItemDeleteView.as_view(), name='cartitem-delete'),

]
