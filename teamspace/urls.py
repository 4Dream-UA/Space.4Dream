from django.urls import path

from .views import AllMembersView


app_name = "teamspace"

urlpatterns = [
    path("all_members", AllMembersView.as_view(), name="all_members"),
]
