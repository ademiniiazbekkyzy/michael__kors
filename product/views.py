from django.shortcuts import render

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = Product.serializers

class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class =Category.serializers
    permission_class = [Isauthenticated]



class CategoryRetriveDeleteUpdateView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    queryset = Categoty.objects.all()
    serializer_class = Category.serializers
    permission_class = [IsAuthenticated]
