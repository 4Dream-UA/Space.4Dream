from django.urls import path


from .views import AllMembersView, CreateTeamView, ListTeamView

app_name = "teamspace"

urlpatterns = [
    path("all_members", AllMembersView.as_view(), name="all_members"),
    path("create_team", CreateTeamView.as_view(), name="create_team"),
    path("teams", ListTeamView.as_view(), name="teams_list"),
]
