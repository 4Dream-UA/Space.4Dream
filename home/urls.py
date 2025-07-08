from django.urls import path
from .views import HomePageView, UpdateSettingsView, CreateInviteView

app_name = "home"

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("settings/<int:pk>", UpdateSettingsView.as_view(), name="settings"),
    path("invite", CreateInviteView.as_view(), name="invite"),
]
