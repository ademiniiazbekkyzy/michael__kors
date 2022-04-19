from django import forms

from product.models import Product


class CreateOrderForm(forms.Form):
    product = forms.ModelChoiceField(Product.objects.all())
    phone = forms.CharField(max_length=13)
    address = forms.CharField(widget=forms.Textarea)
    city = forms.CharField(max_length=100)
    email = forms.EmailField()
