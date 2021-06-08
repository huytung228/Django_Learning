from django.db import models
from django.db.models.base import Model

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=45)
    slug = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    active = models.BooleanField(default=True)


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=45)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    active = models.BooleanField(default=True)


class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=45)
    price = models.IntegerField(default=0)
    sale_price = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    inventory = models.IntegerField(default=0)