from django.contrib.auth import get_user, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import UpdateView
from django.urls import reverse_lazy


class HomePageView(View):
    template_name = "home/index.html"

    def get(self, request):
        return render(request, self.template_name)


class UpdateSettingsView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    fields = [
        "username", "email",
        "first_name", "last_name",
              ]
    template_name = "home/settings.html"
    success_url = reverse_lazy("home:index")

class UpdateUserPassword(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    fields = []