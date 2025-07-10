from django.urls import path


from .views import (
    AllMembersView, CreateTeamView, ListTeamView,
    EditMembersView, DeleteMembersView, EditTeamView
)

app_name = "teamspace"

urlpatterns = [
    path("all_members/", AllMembersView.as_view(), name="all_members"),
    path("edit_menu/<int:pk>/", EditMembersView.as_view(), name="edit_member"),
    path("delete_menu/<int:pk>/", DeleteMembersView.as_view(), name="delete_member"),
    path("teams/", ListTeamView.as_view(), name="teams_list"),
    path("create_team/", CreateTeamView.as_view(), name="create_team"),
    path("update_team/<int:pk>", EditTeamView.as_view(), name="edit_team"),
]
