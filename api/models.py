from django.db import models
from django.contrib.auth.models import User


class Brand(models.Model):
    name = models.CharField(max_length=120)
    category = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=3)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='products_posters')
    brand = models.ForeignKey(Brand, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class OrederHistory(models.Model):
    customer = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    total_price = models.DecimalField(max_digits=10, decimal_places=3)
