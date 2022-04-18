from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter

from rest_framework.generics import *
from rest_framework.mixins import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


from rest_framework.viewsets import ModelViewSet, GenericViewSet, ViewSet

from product.filters import ProductFilter
from product.models import Product, Rating, Category
from product.permissions import IsAdmin, IsAuthor
from product.serializers import ProductSerializer, RatingSerializers, CategorySerializers
class LargeResultsSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = Product.serializers
    pagination_class = LargeResultsSetPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    ordering_fields = ['id', 'price']
    search_fields = ['name', 'description']


    def get_permissions(self):
        print(self.action)
        if self.action in ['list', 'retrieve']:
            permissions = []
        elif self.action == 'rating':
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthenticated]
        return [permissions() for permission in permissions]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def rating(self, request, pk):
        serializer = RatingSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            obj = Rating.objects.get(product=self.get.object(), owner=request.user)
            obj.rating = request.data['rating']
        except Rating.DoesNotExist:
            obj = Rating(owner=request.user, product=self.get_object(), rating=request.data['rating'])
        obj.save()
        return Response(request.data, status=status.HTTP_201_CREATED)




class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class =Category.serializers
    permission_class = [IsAuthenticated]



class CategoryRetriveDeleteUpdateView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    queryset = Category.objects.all()
    serializer_class = Category.serializers
    permission_class = [IsAuthenticated]
