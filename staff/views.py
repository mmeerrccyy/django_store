from django.contrib.auth.models import User
from django.views import generic
from .forms import RegisterForm

# Create your views here.
from staff.mixins import SuperuserRequiredMixin


class StaffView(SuperuserRequiredMixin, generic.ListView):
    model = User
    paginate_by = 2
    template_name = 'admin/staff/list.html'


class StaffUpdate(SuperuserRequiredMixin, generic.UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'is_superuser']
    template_name = 'admin/staff/user/update.html'
    success_url = '/'


class StaffDelete(SuperuserRequiredMixin, generic.DeleteView):
    model = User
    template_name = 'admin/staff/user/confirm_delete.html'
    success_url = '/staff/'


class StaffCreate(SuperuserRequiredMixin, generic.CreateView):
    form_class = RegisterForm
    model = User
    template_name = 'admin/staff/user/add.html'
    success_url = '/staff/'
