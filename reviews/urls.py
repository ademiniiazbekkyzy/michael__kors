from django.urls import path
from . import views

urlpatterns = [
    path('single/<int:pk>', views.new_single, name="new_single"),
]
