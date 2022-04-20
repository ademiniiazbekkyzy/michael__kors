from django.db import models
from rest_framework.authtoken.admin import User

from product.models import Product


class BlogPost(models.Model):
    user = models.ForeignKey(
                User,
                verbose_name="Пользователь",
                on_delete=models.CASCADE, null=True)

    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    likes = models.ManyToManyField(User, related_name='blogpost_like')

    def number_of_likes(self):
        return self.likes.count()
