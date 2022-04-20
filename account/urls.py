from django.urls import path

from product.views import CategoryListCreateView
from .views import *

urlpatterns = [
    # path('category/', CategoryListCreateView.as_view()),
    path('register/', RegisterView.as_view()),
    path('activate/<str:activation_code>/', ActivateView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    # path('change-password/', ChangePasswordView.as_view()),
]