from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.views import *

router = DefaultRouter()
router.register('product', ProductViewSet)

urlpatterns = [
    path('product/v1/api/categories/', CategoryListCreateView.as_view()),
    path('product/categories/<str:slug>/', CategoryRetrieveDeleteUpdateView.as_view()),
    # path('like/', LikeCreateView.as_view(), name='like'),
    # path('comments/', CommentCreateAPI.as_view(), name='comment'),
    # path('comments/<int:pk>/', CommentDetailUpdateDestroyAPI.as_view(), name='comment_detail'),
    path('', include(router.urls))
]




