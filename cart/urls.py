from django.urls import path
from . import views


urlpatterns = [
    path('', views.CartDetail.as_view(), name='cart_detail'),
    path('add/<int:product_id>/', views.CartAdd.as_view(), name='cart_add'),
    path('remove/<int:product_id>/', views.CartRemove.as_view(), name='cart_remove'),
]