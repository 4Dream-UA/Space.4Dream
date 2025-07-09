from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import HomePageView, UpdateSettingsView, CreateInviteView, ProfileView

app_name = "home"

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("settings/<int:pk>", UpdateSettingsView.as_view(), name="settings"),
    path("invite", CreateInviteView.as_view(), name="invite"),
    path("profile", ProfileView.as_view(), name="profile"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
