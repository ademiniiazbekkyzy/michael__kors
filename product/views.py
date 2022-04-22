from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import *
from rest_framework.mixins import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from product.filters import ProductFilter
from product.models import Product, Rating, Category
from product.serializers import RatingSerializers, CategorySerializers, ProductSerializers
# from .permissions import IsAdmin, IsUserOrReadOnly


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    pagination_class = LargeResultsSetPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    ordering_fields = ['id', 'price']
    search_fields = ['name', 'description']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions = []
        elif self.action == 'rating':
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(methods=['POST'], detail=True)
    def rating(self, request, pk):  # http://localhost:8000/product/id_product/rating/
        serializer = RatingSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            obj = Rating.objects.get(product=self.get_object(),
                                     owner=request.user)
            obj.rating = request.data['rating']
        except Rating.DoesNotExist:
            obj = Rating(owner=request.user,
                         product=self.get_object(),
                         rating=request.data['rating']
                         )
        obj.save()
        return Response(request.data,
                        status=status.HTTP_201_CREATED)


class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_class = [IsAuthenticated]


class CategoryRetrieveDeleteUpdateView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_class = [IsAuthenticated]


# class CommentCreateAPI(ListCreateAPIView):
#     serializer_class = CommentsSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     queryset = Comment.objects.all()
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
#
#
# class CommentDetailUpdateDestroyAPI(RetrieveUpdateDestroyAPIView):
#     serializer_class = CommentsSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly, IsUserOrReadOnly]
#     queryset = Comment.objects.all()

# class LikeCreateView(ListCreateAPIView):
#     serializer_class = LikeSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly, IsUserOrReadOnly]
#     queryset = Like.objects.all()
#
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         if serializer.validated_data:
#             serializer.validated_data['user'] = request.user
#             print(serializer.data)
#             obj, created = Like.objects.get_or_create(**serializer.validated_data)
#             if not created:
#                 obj.delete()
#                 return Response([])
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

