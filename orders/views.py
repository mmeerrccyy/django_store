from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.utils.decorators import method_decorator

from cart.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItem, Order
from .tasks import order_created


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
            order_created.delay(order.id)
            return render(request, 'orders/order/created.html',
                          {'order': order})

    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        form = OrderCreateForm()
        context = {
            'cart': cart,
            'form': form
        }
        return render(request, 'orders/order/create.html', context)


class AdminOrderDetail(View):
    @method_decorator(staff_member_required)
    def get(self, request, *args, **kwargs):
        order = get_object_or_404(Order, id=kwargs.get('order_id'))
        return render(request, 'admin/orders/order/detail.html', {'order': order})


class OrderList(View):
    @method_decorator(staff_member_required)
    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()
        return render(request, 'admin/orders/list.html', {'orders': orders})