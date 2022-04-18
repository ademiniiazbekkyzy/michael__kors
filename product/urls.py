from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.views import *

router = DefaultRouter()
router.register = ('', ProductViewSet)

from product.views import *
urlpatterrns = [
    path('category/', CategoryListCreateView.as_view()),
    path('category/<str:slug>', CategoryRetriveDeleteUpdateView.as_view()),
    path('', include(router.urls))
]
