from django.contrib import admin

from product.models import *

admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Rating)
# admin.site.register(Reviews)


class ImageInAdmin(admin.TabularInline):
    model = Image
    fields = ('image',)
    max_num = 5


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ImageInAdmin
    ]
