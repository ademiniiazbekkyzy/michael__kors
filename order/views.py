from django.shortcuts import render
from rest_framework.decorators import api_view

from order.forms import CreateOrderForm
from order.models import Order

@api_view(['GET'])
def create_order(request):
    order_form = CreateOrderForm(request.POST)
    if order_form.is_valid():
        order = Order.objects.create(order_form.cleaned_data)
        return render(request, 'order/')
    order_form = CreateOrderForm
    return render(request, 'order/')
