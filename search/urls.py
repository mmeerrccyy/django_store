from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.SearchResult.as_view(), name='search_results'),
]
