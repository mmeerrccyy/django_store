from django.urls import path

from . import views

urlpatterns = [
    path('', views.StaffView.as_view(), name='staff_list'),
    path('create/', views.StaffCreate.as_view(), name='staff_create'),
    path('edit/<int:pk>/', views.StaffUpdate.as_view(), name='staff_update'),
    path('delete/<int:pk>/', views.StaffDelete.as_view(), name='staff_delete')
]
