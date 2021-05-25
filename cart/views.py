from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
# Create your views here.


class CartAdd(View):
    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        product = get_object_or_404(Product, id=kwargs.get('product_id'))
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product,
                     quantity=cd['quantity'],
                     update_quantity=cd['update'])
        return redirect('cart_detail')


class CartRemove(View):
    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        product = get_object_or_404(Product, id=kwargs.get('product_id'))
        cart.remove(product)
        return redirect('cart_detail')


class CartDetail(View):
    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        return render(request, 'cart/detail.html', {'cart': cart})

