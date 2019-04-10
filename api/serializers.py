from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Category, Product, Order, Profile, Address, CartItem, Image


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


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    # images = ImageSerializer(many=True)
    # print(images)

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'price',
                  'description', 'stock', 'images']

    def get_images(self, obj):
        queryset = Image.objects.filter(product=obj)
        images = ImageSerializer(
            queryset, many=True, context=self.context).data
        print(self)
        print(self.context)
        print(self.context.get("images"))
        print(obj.images.all())
        print(images)
        return images


class CartItemDetailSerializer(serializers.ModelSerializer):
    product = ProductDetailSerializer()

    class Meta:
        model = CartItem
        fields = '__all__'


class OrderCreateSerializer(serializers.ModelSerializer):
    cartItems = CartItemDetailSerializer(many=True)

    class Meta:
        model = Order
        fields = ['cartItems', 'date', 'time', 'total_price']


class ProductListSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    # print(images)

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'price', 'images', 'stock']


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class CartItemDetailSerializer(serializers.ModelSerializer):
    product = ProductDetailSerializer()

    class Meta:
        model = CartItem
        fields = '__all__'


class CartItemCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['product', 'quantity', 'order']


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
        fields = ['id', 'product', 'order']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'description']


class ProfileDetailSerializer(serializers.ModelSerializer):
    update = serializers.HyperlinkedIdentityField(
        view_name="api-update",
        lookup_field="id",
        lookup_url_kwarg="profile_id"
    )
    addresses = AddressSerializer(many=True)

    class Meta:
        model = Profile
        fields = [
            'dob',
            'gender',
            'addresses',
            'update',
        ]


class ProfileCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'dob',
            'gender',
        ]


class OrderListSerializer(serializers.ModelSerializer):

        # total_price = serializers.SerializerMethodField()
    cartItems = serializers.SerializerMethodField()
    detail = serializers.HyperlinkedIdentityField(
        view_name="api-order-detail",
        lookup_field="id",
        lookup_url_kwarg="order_id"
    )

    class Meta:
        model = Order
        fields = [
            'id',
            'profile',
            'timestamp',
            'total_price',
            'cartItems',
            'detail',
        ]

    def get_cartItems(self, obj):
        cartItems = CartItem.objects.filter(order=obj)
        item_list = CartItemDetailSerializer(
            cartItems, many=True, context=self.context).data
        return item_list


class OrderDetailSerializer(serializers.ModelSerializer):
    cartItems = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = '__all__'

    def get_cartItems(self, obj):
        cartItems = CartItem.objects.filter(order=obj)
        item_list = CartItemDetailSerializer(cartItems, many=True).data
        return item_list
