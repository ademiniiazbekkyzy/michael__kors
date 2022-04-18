from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
# from django.db.models import SmallIntegerField
from django.db.models import SmallIntegerField

User = get_user_model()

class Category(models.Model):
    slug = models.SlugField(max_length=30, primary_key=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.slug

class Product(models.Model):
    owner = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimallField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='images')
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)


class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASADE, related_name='ratings')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    rating = SmallIntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ])

