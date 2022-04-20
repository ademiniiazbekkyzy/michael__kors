from django.contrib.auth import get_user_model
from django.db import models
from product.models import Product

User = get_user_model()


class Comments(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE)
    new = models.ForeignKey(
         Product,
         verbose_name="Товар",
         on_delete=models.CASCADE)
    text = models.TextField("Отзыв")
    created = models.DateTimeField("Дата добавления", auto_now_add=True, null=True)
    moderation = models.BooleanField("Модерация", default=False)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def __str__(self):
        return "{}".format(self.user)
