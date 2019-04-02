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


class CategoryDetail(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'category_id'


class CategoryCreate(CreateAPIView):
    serializer_class = CategoryCreateUpdateSerializer


class CategoryUpdate(RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'category_id'


class CategoryDelete(DestroyAPIView):
    queryset = Category.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'category_id'


class CartItemsList(ListAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemListSerializer


class CartItemDetail(RetrieveAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'cartItem_id'


class CartItemCreate(CreateAPIView):
    serializer_class = CartItemCreateUpdateSerializer


class CartItemUpdate(RetrieveUpdateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemCreateUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'cartItem_id'


class CartItemDelete(DestroyAPIView):
    queryset = CartItem.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'cartItem_id'
