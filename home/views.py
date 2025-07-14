from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import UpdateView, CreateView, ListView, DetailView
from django.urls import reverse_lazy

from .forms import RegisterInviteForm


class HomePageView(ListView):
    model = get_user_model()
    context_object_name = "users"
    template_name = "home/index.html"



class CreateInviteView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = get_user_model()
    form_class = RegisterInviteForm
    template_name = "home/invite.html"
    success_url = reverse_lazy("home:index")

    def test_func(self) -> bool:
        if self.request.user.is_staff:
            return True
        return False

class UpdateSettingsView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    fields = [
        "first_name", "last_name",
        "avatar"
              ]
    template_name = "home/settings.html"
    success_url = reverse_lazy("home:index")

class ProfileView(LoginRequiredMixin, ListView):
    model = get_user_model()
    template_name = "home/profile.html"


class UserDetailView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = "home/user_detail.html"
    context_object_name = "d_user"
