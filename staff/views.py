from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import generic
from django.views.generic.base import View


# Create your views here.


class StaffView(View):

    def get(self, request):
        staff_users = User.objects.filter(is_staff=True)
        context = {
            "staff_users": staff_users
        }
        return render(request, 'admin/staff/list.html', context)


class StaffUpdate(generic.UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'is_superuser']
    template_name = 'admin/staff/user/update.html'
    success_url = '/'


# class StaffCreate(generic.CreateView):
#     model = User
#     fields = ['username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'is_superuser']
#     # template_name = 'admin/staff/user/update.html'
