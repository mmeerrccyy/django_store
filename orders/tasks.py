from celery import shared_task
from django.core.mail import send_mail

from .models import Order


@shared_task
def order_created(order_id):
    """
    Відправлення листа про замовлення.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Order #{order.id}'
    message = f'Dear {order.first_name},\n\nYou have successfully placed an order.\
                Your order id is {order.id}.'
    mail_sent = send_mail(subject, message, 'no_reply@myshop.com', [order.email])
    return mail_sent
