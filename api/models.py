from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, post_delete, pre_delete


class Category(models.Model):
	name = models.CharField(max_length=120)

	def __str__(self):
		return self.name


# profile
# has whatever data you want eg dob, email
# foreign key of the user


class Profile(models.Model):
	user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
	dob = models.DateField(null=True)
	GENDERS = (
		('M', 'Male'),
		('F', 'Female'),
	)
	gender = models.CharField(
		max_length=2,
		choices=GENDERS,
		default='F',
	)

	def __str__(self):
		return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwarg):
	if created:
		Profile.objects.create(user=instance)


# address
# forign key of the profile and has a related name
# address detail related
class Address(models.Model):
	profile = models.ForeignKey(
		Profile, related_name='addresses', default=1, on_delete=models.CASCADE)
	description = models.TextField()


class Product(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField()
	stock = models.IntegerField(default=0)

	category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=10, decimal_places=3, default=0)

	def __str__(self):
		return self.name


	# def image(self):
	#     return self.images.first()

# Varient model
# product as a foreign key and add a related name
# has a price--> you have to remove the price from the `product`
# varient name
# Description (s,m,xl) blank=true


class Order(models.Model):
	profile = models.ForeignKey(
		Profile, related_name='orders', default=1, on_delete=models.CASCADE)
	date = models.DateField()
	time = models.TimeField()
	total_price = models.DecimalField(max_digits=10, decimal_places=3, default=0)


	# def get_total_price(self, sentValue):
	# 	cartItems = 
	# 	new_total_price = self.total_price + sentValue
	# 	return new_total_price

	# def get_total_price(self, sentValue):
	# 	new_total_price = self.total_price + sentValue
	# 	return new_total_price

		 # return self.total_price += sentValue

# takes the profile as a foreign key
# takes the order as a foreign key has a related name
# takes the Varient as a foriegn key
# takes quantity as an iteger
# total price is an integer and is the total of quantity * the product price

class CartItem(models.Model):
	# profile = models.ForeignKey(Profile, default=1, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, default=1, on_delete=models.CASCADE)
	order = models.ForeignKey(
		Order, related_name='cartItems', default=1, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=0)
	sub_total = models.DecimalField(max_digits=10, decimal_places=3, default=0)
	STATUS = (
		('C', 'Cart'),
		('O', 'Ordered'),
		('P', 'Processed'),
		('S', 'Shipped'),
	)
	status = models.CharField(
		max_length=2,
		choices=STATUS,
		default='C',
	)

@receiver(pre_save, sender=CartItem)
def get_sub_total(instance, *args, **kwargs):
	instance.sub_total = instance.quantity * instance.product.price



@receiver(post_save, sender=CartItem)
def update_total_stock(sender, instance, created, **kwargs):
	if (instance.product.stock >= instance.quantity):
		instance.order.total_price += instance.sub_total
		instance.product.stock -= instance.quantity
		instance.product.save()
		instance.order.save()
	else:
		instance.quantity = 0
		instance.sub_total=0.000
		instance.save()
		instance.delete()



@receiver(pre_delete, sender=CartItem)
def delete_total_stock(sender, instance, **kwargs):
	# if (instance.product.stock > instance.quantity):
	instance.product.stock += instance.quantity
	instance.order.total_price -= instance.sub_total
	instance.product.save()
	instance.order.save()

	# if created:
	# 	return instance.order.get_total_price(instance.sub_total)




# ----------***added an image field***------------


class Image(models.Model):

	product = models.ForeignKey(
		Product, related_name='images', default=1, on_delete=models.CASCADE)

	image = models.ImageField(
		upload_to='products_photos', null=True, blank=True)

<<<<<<< HEAD
    def __str__(self):
        return self.product.name
=======
	def __str__(self):
		return self.product
>>>>>>> cf06baa3b1d75350a1f0d9041e8f44aba8a9ed5e
