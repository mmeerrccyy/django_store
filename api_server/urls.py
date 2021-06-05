from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import UsernameValidation

urlpatterns = [
    path('validate-username/', csrf_exempt(UsernameValidation.as_view()), name='validate_username'),
]