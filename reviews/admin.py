from django.contrib import admin
from product.models import Product
from reviews.models import Comments


class CommentAdmin(admin.ModelAdmin):
    """ Комментарии
    """
    list_display = ('user', 'new', 'created', 'moderation')


admin.site.register(Comments, CommentAdmin)


