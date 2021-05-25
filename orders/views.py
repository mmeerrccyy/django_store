from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from django.views.generic.base import View
from cart.cart import Cart

# Create your views here.


class OrderCreate(View):
    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            return render(request, 'orders/order/created.html',
                          {'order': order})

    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        form = OrderCreateForm()
        context = {
            'cart': cart,
            'form': form
        }
        return render(request, 'orders/order/created.html', context)