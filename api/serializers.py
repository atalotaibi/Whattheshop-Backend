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


class CategorySerialzer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class ImageSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
    class Meta:
        model = Image
        exclude = ['product']


class ProductListSerializer(serializers.ModelSerializer):
    category = CategorySerialzer()
    images = ImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'price', 'images']

    def get_category(self, obj):
        category = obj.name
        return category


class ProductDetailSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'price',
                  'description', 'stock', 'images']


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
=======
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
>>>>>>> cf06baa3b1d75350a1f0d9041e8f44aba8a9ed5e


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
		fields = ['product', 'quantity', 'sub_total']


class CartItemCreateUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = CartItem
		fields = ['product', 'quantity', 'sub_total']


class AddressSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
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
=======
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
>>>>>>> cf06baa3b1d75350a1f0d9041e8f44aba8a9ed5e

#  ..... Order Model ....
# profile = models.ForeignKey(Profile, related_name='orders', default=1, on_delete=models.CASCADE)
# date = models.DateField()
# time = models.TimeField()
#     def total_price(self):
#         return sum(self.cartItems.all().sub_total)


class OrderListSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
    total_price = serializers.SerializerMethodField()
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

    def get_total_price(self, obj):
        return str(obj.total_price())
=======
	# total_price = serializers.SerializerMethodField()
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
		item_list = CartItemDetailSerializer(cartItems, many=True).data
		return item_list

	# def get_total_price(self, obj):
	# 	return str(obj.get_total_price())
>>>>>>> cf06baa3b1d75350a1f0d9041e8f44aba8a9ed5e


class OrderDetailSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
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
=======
	# profile = ProfileSerializer() 
	cartItems = serializers.SerializerMethodField()
	class Meta:
		model = CartItem
		fields = '__all__'
	def get_cartItems(self, obj):
		cartItems = CartItem.objects.filter(order=obj)
		item_list = CartItemListSerializer(cartItems, many=True).data
		return item_list

>>>>>>> cf06baa3b1d75350a1f0d9041e8f44aba8a9ed5e
