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

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id','description']        

class ProfileDetailSerializer(serializers.ModelSerializer):
    update = serializers.HyperlinkedIdentityField(
        view_name = "api-update",
        lookup_field = "id",
        lookup_url_kwarg = "profile_id"
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
