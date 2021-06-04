from django import forms

from .models import Product, Category


class ProductAddForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'slug', 'image', 'description', 'price', 'stock', 'available']


class CategoryAddForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug']