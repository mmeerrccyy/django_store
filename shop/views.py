from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View

from cart.forms import CartAddProductForm
from .models import Category, Product


# Create your views here.

class ProductList(View):

    def get(self, request, *args, **kwargs):
        category = None
        category_slug = kwargs.get('category_slug')
        categories = Category.objects.all()
        products = Product.objects.filter(available=True)
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)
        context = {
            'category': category,
            'categories': categories,
            'products': products,
        }
        return render(request, 'shop/product/list.html', context)


class ProductCategory(View):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        products = Product.objects.filter(available=True)
        category = get_object_or_404(Category, slug=kwargs.get('category_slug'))
        products = products.filter(category=category)
        context = {
            'category': category,
            'products': products,
            'categories': categories,
        }
        return render(request, 'shop/product/list.html', context)


class ProductDetail(View):

    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, slug=kwargs.get('slug'), available=True)
        cart_product_form = CartAddProductForm()
        context = {
            'product': product,
            'cart_product_form': cart_product_form
        }
        return render(request, 'shop/product/detail.html', context)