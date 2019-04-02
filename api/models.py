from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


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

    def total_price(self):
        return sum(self.cartItems.all().sub_total)


# cartitem
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

    def sub_total(self):
        return self.quantity * product.price

# ----------***added an image field***------------

class Image(models.Model):
    image = models.ImageField(upload_to='products_photos', null=True, blank=True)
    product = models.ForeignKey(
        Product, related_name='images', default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.product

