from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.OrderCreate.as_view(), name='order_create'),
    url(r'^admin/order/(?P<order_id>\d+)/$', views.AdminOrderDetail.as_view(), name='admin_order_detail'),
]
