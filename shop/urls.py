from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductList.as_view(), name='product_list'),
    path('category/<str:category_slug>/', views.ProductCategory.as_view(), name='products_list_by_category'),
    path('product/<str:category_slug>/<str:slug>/', views.ProductDetail.as_view(), name='product_detail'),
    path('product/add/', views.ProductCreate.as_view(), name='product_create'),
    path('update/<int:pk>/', views.ProductUpdate.as_view(), name='product_update'),
    path('delete/<int:pk>/', views.ProductDelete.as_view(), name='product_delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
