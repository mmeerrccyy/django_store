from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView
from django.views.generic.base import View
# Create your views here.
from shop.models import Product


class SearchResult(ListView):
    model = Product
    template_name = 'search/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        return object_list