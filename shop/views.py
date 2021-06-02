from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.base import View

from cart.forms import CartAddProductForm
from .forms import ProductAddForm
from .models import Category, Product
from staff.mixins import SuperuserRequiredMixin


# Create your views here.

class ProductList(View):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        products = Product.objects.filter(available=True)
        paginator = Paginator(products, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'categories': categories,
            'products': products,
            'page_obj': page_obj
        }
        return render(request, 'shop/product/list.html', context)


class ProductCategory(View):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        products = Product.objects.filter(available=True)
        category = get_object_or_404(Category, slug=kwargs.get('category_slug'))
        products = products.filter(category=category)
        paginator = Paginator(products, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'category': category,
            'products': products,
            'categories': categories,
            'page_obj': page_obj
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


class ProductCreate(SuperuserRequiredMixin, generic.CreateView):
    model = Product
    template_name = 'admin/shop/product/add.html'
    form_class = ProductAddForm
    success_url = '/'


class ProductUpdate(SuperuserRequiredMixin, generic.UpdateView):
    model = Product
    fields = ['category', 'name', 'slug', 'image', 'description', 'price', 'stock', 'available']
    template_name = 'admin/shop/product/update.html'
    success_url = '/'


class ProductDelete(SuperuserRequiredMixin, generic.DeleteView):
    model = Product
    template_name = 'admin/shop/product/confirm_delete.html'
    success_url = '/'