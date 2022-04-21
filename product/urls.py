from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.views import *

router = DefaultRouter()
router.register('product', ProductViewSet)

urlpatterns = [
    path('product/v1/api/categories/', CategoryListCreateView.as_view()),
    path('product/categories/<str:slug>/', CategoryRetrieveDeleteUpdateView.as_view()),
    # path('single/<int:pk>/', views.new_single),
    path('', include(router.urls))
]

print(router.urls)

