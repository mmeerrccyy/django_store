from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.OrderCreate.as_view(), name='order_create'),
    path('list/', views.OrderList.as_view(), name='orders_list'),
    path('detail/<int:order_id>/', views.AdminOrderDetail.as_view(), name='admin_order_detail'),
    path('remove/<int:order_id>/', views.AdminOrderRemove.as_view(), name='admin_order_remove'),
    path('update/<int:pk>/', views.AdminOrderUpdate.as_view(), name='admin_order_update'),
]
