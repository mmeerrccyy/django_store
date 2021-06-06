import json

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.generic.base import View
from shop.models import Category, Product


# Create your views here.

class UsernameValidation(View):

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        username = data['username']
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'username already exists!'}, status=400)
        return JsonResponse({'username_valid': True})


class SlugValidation(View):

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        slug = data['slug']
        if Category.objects.filter(slug=slug).exists() or Product.objects.filter(slug=slug).exists():
            return JsonResponse({'slug_error': 'slug already exists!'}, status=400)
        return JsonResponse({'slug_valid': True})