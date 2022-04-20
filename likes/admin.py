from django.contrib import admin

# Register your models here.
from likes.models import BlogPost

admin.site.register(BlogPost)