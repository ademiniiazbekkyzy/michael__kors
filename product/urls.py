from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.views import *

router = DefaultRouter()
router.register = ('product', ProductViewSet)

urlpatterns = [
    path('v1/api/categories/', CategoryListCreateView.as_view()),
    path('categories/<str:slug>/', CategoryRetrieveDeleteUpdateView.as_view()),
    path('', include(router.urls))
]

