from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'is_superuser', 'password']
        widgets = {
            'password': forms.PasswordInput(),
            'email': forms.EmailInput()
        }
