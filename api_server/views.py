import json

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.generic.base import View


# Create your views here.

class UsernameValidation(View):

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        username = data['username']
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'username already exists!'}, status=400)
        return JsonResponse({'username_valid': True})
