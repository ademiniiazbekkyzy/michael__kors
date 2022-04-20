from django.urls import path
from . import views
from .views import (

    BlogPostLike,

)

urlpatterns = [

    path('blogpost-like/<int:pk>', views.BlogPostLike, name="blogpost_like"),

]