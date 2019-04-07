from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.views import APIView
from .models import Category, Product, Order, Profile, Address, CartItem
from .serializers import (
    UserCreateSerializer,
    CategoryListSerializer,
    CartItemDetailSerializer,
    CartItemCreateUpdateSerializer,
    AddressSerializer,
    ProfileDetailSerializer,
    ProfileCreateUpdateSerializer,
)
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .serializers import (OrderListSerializer, OrderDetailSerializer,
                          ProductListSerializer, ProductDetailSerializer,)
from rest_framework import status
from rest_framework.response import Response
from django.http import QueryDict


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
    # permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)


class OrderListView(ListAPIView):
    serializer_class = OrderListSerializer

    def get_queryset(self):
        return Order.objects.filter(profile=self.request.user.profile)


class OrderDetailView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'order_id'


class CartItemCreateView(CreateAPIView):
    serializer_class = CartItemCreateUpdateSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        # print(request.data)
        new_data = QueryDict.dict(data)
        # print(new_data)
        # print(new_data['product'])
        # print(new_data['order'])
        # print(new_data['quantity'])
        order_id = new_data['order']
        # print(kwargs)
        serializer = self.serializer_class(data=data)
        print(serializer)
        if serializer.is_valid():
            valid_data = serializer.data
            # print(valid_data)
            # print(serializer.errors)
            # print(valid_data['product'])
            # print(valid_data['quantity'])
            new_data = {
                'product': Product.objects.get(id=valid_data['product']),
                'order': Order.objects.get(id=order_id)
            }
            cartItem, created = CartItem.objects.get_or_create(**new_data)
            if created:
                cartItem.quantity = valid_data['quantity']
                cartItem.save()
                cartItem.product.stock -= cartItem.quantity
                cartItem.product.save()
                return Response(valid_data, status=status.HTTP_200_OK)
            else:
                # print("stock before")
                # print(cartItem.product.stock)
                cartItem.product.stock += cartItem.quantity
                # print("stock after")
                # print(cartItem.product.stock)
                # print("quantity before:")
                # print(cartItem.quantity)
                cartItem.quantity = 0
                cartItem.quantity += valid_data['quantity']
                # print("quantity after")
                # print(cartItem.quantity)
                cartItem.save()
                cartItem.product.stock = cartItem.product.stock - cartItem.quantity
                # print("stock after again2")
                # print(cartItem.product.stock)
                cartItem.product.save()
                return Response(valid_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartItemUpdateView(RetrieveUpdateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemCreateUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'cartItem_id'

    def put(self, request, *args, **kwargs):
        my_data = request.data
        cartItem_id = kwargs
        # print(kwargs)
        # print(cartItem_id['cartItem_id'])
        serializer = self.serializer_class(data=my_data)
        if serializer.is_valid():
            valid_data = serializer.data
            cartItem = CartItem.objects.get(id=cartItem_id['cartItem_id'])
            # print(cartItem)
            cartItem.product.stock += cartItem.quantity
            cartItem.quantity = valid_data['quantity']
            cartItem.save()
            cartItem.product.stock -= cartItem.quantity
            cartItem.product.save()
            return Response(valid_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartItemDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemCreateUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'cartItem_id'

    # def destroy(self, request, *args, **kwargs):
    #     my_data = request.data
    #     cartItem_id = kwargs
    #     serializer = self.serializer_class(data=my_data)
    #     if serializer.is_valid():
    #         valid_data = serializer.data
    #         cartItem = CartItem.objects.get(id=cartItem_id['cartItem_id'])
    #         cartItem.product.stock += cartItem.quantity
    #         cartItem.delete()
    #         cartItem.product.save()
    #         return Response(valid_data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
