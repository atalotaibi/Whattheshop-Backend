from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, post_delete, pre_delete


class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
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


class Address(models.Model):
    profile = models.ForeignKey(
        Profile, related_name='addresses', default=1, on_delete=models.CASCADE)
    description = models.TextField()


class Product(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    stock = models.IntegerField(default=0)

    category = models.ForeignKey(
        Category, related_name='products', default=1, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=3, default=0)

    def __str__(self):
        return self.name


class Order(models.Model):
    profile = models.ForeignKey(
        Profile, related_name='orders', default=1, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(
        max_digits=10, decimal_places=3, default=0)
    completed = models.BooleanField(default=False)

    def update_total(self):
        self.total_price = sum(self.cartItems.all(
        ).values_list('sub_total', flat=True))
        self.save()


class CartItem(models.Model):
    product = models.ForeignKey(Product, default=1, on_delete=models.CASCADE)
    order = models.ForeignKey(
        Order, related_name='cartItems', default=1, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
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
@receiver(post_delete, sender=CartItem)
def update_total(sender, instance, *args, **kwargs):
    instance.order.update_total()


class Image(models.Model):
    product = models.ForeignKey(
        Product, related_name='images', default=1, on_delete=models.CASCADE)

    image = models.ImageField(
        upload_to='products_photos', null=True, blank=True)

    def __str__(self):
        return self.product.name
