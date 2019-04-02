from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Category, Product, Order, Profile, Address, CartItem

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        return validated_data


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class CategoryDetailSerializer(serializers.ModelSerializer):
    # products = ProductSerializer(many=True)

    class Meta:
        model = Category
    # fields =  ['name', 'category','products']
        fields = ['name', 'category']


class CategoryCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'category']


class CartItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'product']


class CartItemDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ['product', 'varient', 'quantity', 'total_price']


class CartItemCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['product', 'varient', 'quantity', 'total_price']

#  ..... Order Model .... 
# profile = models.ForeignKey(Profile, related_name='orders', default=1, on_delete=models.CASCADE)
# date = models.DateField()
# time = models.TimeField()
#     def total_price(self):
#         return sum(self.cartItems.all().sub_total)

class OrderListSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    cartItems = serializers.SerializerMethodField()
    detail = serializers.HyperlinkedIdentityField(
        view_name = "api-order-detail",
        lookup_field = "id",
        lookup_url_kwarg = "order_id"
        )
    class Meta:
        model = Order
        fields = [
            'id',
            'profile',
            'date',
            'time',
            'total_price',
            'cartItems',
            'detail',
            ]
    def get_cartItems(self, obj):
        cartItems = CartItem.objects.filter(order=obj)
        item_list = CartItemListSerializer(cartItems, many=True).data
        return item_list

class OrderDetailSerializer(serializers.ModelSerializer):
    # profile = ProfileSerializer() 
    class Meta:
        cartItems = serializers.SerializerMethodField()
        model = Order
        fields = [
            'id',
            'date',
            'time',
            # 'total_price',
            'cartItems',
            ]
    def get_cartItems(self, obj):
        cartItems = CartItem.objects.filter(order=obj)
        item_list = CartItemListSerializer(cartItems, many=True).data
        return item_list
