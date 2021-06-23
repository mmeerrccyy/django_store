from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.base import View

from cart.forms import CartAddProductForm
from .forms import ProductAddForm, CategoryAddForm
from .models import Category, Product


# Create your views here.

class ProductList(View):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        products = Product.objects.filter(available=True)
        paginator = Paginator(products, 10)
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
        paginator = Paginator(products, 10)
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
        print(request, args, kwargs)
        product = get_object_or_404(Product, slug=kwargs.get('slug'), available=True)
        cart_product_form = CartAddProductForm()
        context = {
            'product': product,
            'cart_product_form': cart_product_form
        }
        return render(request, 'shop/product/detail.html', context)


class ProductCreate(LoginRequiredMixin, generic.CreateView):
    model = Product
    template_name = 'admin/shop/product/add.html'
    form_class = ProductAddForm
    success_url = '/'


class ProductUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Product
    fields = ['category', 'name', 'slug', 'image', 'description', 'price', 'stock', 'available']
    template_name = 'admin/shop/product/update.html'
    success_url = '/'


class ProductDelete(LoginRequiredMixin, generic.DeleteView):
    model = Product
    template_name = 'admin/shop/product/confirm_delete.html'
    success_url = '/'


class ProductArchiveList(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        products = Product.objects.filter(available=False)
        paginator = Paginator(products, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'categories': categories,
            'products': products,
            'page_obj': page_obj
        }
        return render(request, 'admin/shop/list_archive.html', context)


class ProductArchiveDetail(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, slug=kwargs.get('slug'), available=False)
        cart_product_form = CartAddProductForm()
        context = {
            'product': product,
            'cart_product_form': cart_product_form
        }
        return render(request, 'shop/product/detail.html', context)


class ProductArchiveCategory(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        products = Product.objects.filter(available=False)
        category = get_object_or_404(Category, slug=kwargs.get('category_slug'))
        products = products.filter(category=category)
        paginator = Paginator(products, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'category': category,
            'products': products,
            'categories': categories,
            'page_obj': page_obj
        }
        return render(request, 'admin/shop/list_archive.html', context)


class CategoryAdd(LoginRequiredMixin, generic.CreateView):
    model = Category
    template_name = 'admin/shop/category/add.html'
    form_class = CategoryAddForm
    success_url = '/'


class CategoryDelete(LoginRequiredMixin, generic.DeleteView):
    model = Category
    template_name = 'admin/shop/category/confirm_delete.html'
    success_url = '/'


class CategoryUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Category
    template_name = 'admin/shop/category/update.html'
    fields = ['name', 'slug']
    success_url = '/'
