from django_filters import rest_framework as filters

from product.models import Product

class ProductFilter(filters.FilterSet):
    name = filters.CharField(field_name='name', lookup_expr='icontains')
    price_from = filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_to = filters.NumberFilter(field_name='price', lookup_expr='lte')


class Meta:
    model = Product
    fields = ('category', 'name', 'price_from', 'price_to')