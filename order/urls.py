from django.urls import path

from order.views import create_order

urlpatterns = [
    path('create/', create_order, name='create-order'),
]


