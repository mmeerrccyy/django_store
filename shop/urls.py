from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductList.as_view(), name='product_list'),
    path('category/<str:category_slug>/', views.ProductCategory.as_view(), name='products_list_by_category'),
    path('<int:id>/<str:slug>/', views.ProductDetail.as_view(), name='product_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)