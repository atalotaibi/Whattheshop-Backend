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
    CartItemCreateUpdateSerializer,

    AddressSerializer,
    ProfileDetailSerializer,
    ProfileCreateUpdateSerializer,
)
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .serializers import (OrderListSerializer, OrderDetailSerializer,
                          ProductListSerializer, ProductDetailSerializer,)


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class CategorysList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'product_id'


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

class ProfileDetailView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'profile_id'


class ProfileUpdateView(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileCreateUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'profile_id'


# class AddressListlView(RetrieveAPIView):
#     queryset = Address.objects.filter(profile=profile_id)
#     serializer_class = AddressSerializer
#     # lookup_field = 'profile'
#     lookup_url_kwarg = 'profile_id'

class AddressListlView(ListAPIView):
    serializer_class = AddressSerializer

    def get_queryset(self):
        return Address.objects.filter(profile=self.kwargs['profile_id'])


class AddressUpdateView(RetrieveUpdateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'address_id'


class AddressDeleteView(DestroyAPIView):
    queryset = Address.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'address_id'


class AddressCreateView(CreateAPIView):
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user)


class OrderListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer


class OrderDetailView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'order_id'
