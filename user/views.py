from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.shortcuts import redirect

from user.forms import GenerateRandomUsersForm
from user.tasks import generate_random_users


class UsersListView(ListView):
    template_name = 'user/users_list.html'
    model = User


class GenerateRandomUserView(FormView):
    template_name = 'user/random_generate.html'
    form_class = GenerateRandomUsersForm

    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        generate_random_users.delay(total)
        messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')
        return redirect("user-list")