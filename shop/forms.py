from django import forms

from .models import Product


class ProductAddForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'slug', 'image', 'description', 'price', 'stock', 'available']
