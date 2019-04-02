from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
)
from .models import Category, Product, Order, Profile, Address, CartItem
from .serializers import (
    UserCreateSerializer,
    CategoryListSerializer,
    CategoryDetailSerializer,
    CategoryCreateUpdateSerializer,
    CartItemListSerializer,
    CartItemDetailSerializer,
    CartItemCreateUpdateSerializer
)


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class CategorysList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


# class CategoryCreate(CreateAPIView):
#     serializer_class = CategoryCreateUpdateSerializer


# class CategoryUpdate(RetrieveUpdateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategoryCreateUpdateSerializer
#     lookup_field = 'id'
#     lookup_url_kwarg = 'category_id'


# class CategoryDelete(DestroyAPIView):
#     queryset = Category.objects.all()
#     lookup_field = 'id'
#     lookup_url_kwarg = 'category_id'
