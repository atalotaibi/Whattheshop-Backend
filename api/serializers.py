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


class ProductListSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many = True)
    class Meta:
        model = Product
        fields = ['name', 'category', 'price','images']


class ProductDetailSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many = True)
    class Meta:
        model = Product
        fields = ['id','name', 'category', 'price','description', 'stock','images']


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
