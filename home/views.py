from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import UpdateView, CreateView, ListView
from django.urls import reverse_lazy

from config.public_config import invite_able_returning
from .forms import RegisterInviteForm


class HomePageView(View):
    template_name = "home/index.html"

    def get(self, request):
        return render(request, self.template_name)


class CreateInviteView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = get_user_model()
    form_class = RegisterInviteForm
    template_name = "home/invite.html"
    success_url = reverse_lazy("home:index")

    def test_func(self) -> bool:
        if self.request.user.position.name in invite_able_returning():
            return True
        return False

class UpdateSettingsView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    fields = [
        "username", "email",
        "first_name", "last_name",
        "avatar"
              ]
    template_name = "home/settings.html"
    success_url = reverse_lazy("home:index")

class ProfileView(LoginRequiredMixin, ListView):
    model = get_user_model()
    template_name = "home/profile.html"
