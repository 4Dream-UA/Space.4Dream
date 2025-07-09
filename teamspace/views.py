from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

from .models import Project, Team
from config.public_config import invite_able_returning


class AllMembersView(LoginRequiredMixin, ListView):
    model = Team
    context_object_name = "all_members"
    template_name = "teamspace/all_members.html"


class CreateProjectView(LoginRequiredMixin, CreateView):
    model = Project
    ...


class CreateTeamView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Team
    fields = '__all__'
    template_name = "teamspace/create_team.html"
    success_url = reverse_lazy("teamspace:all_members")

    def test_func(self) -> bool:
        if self.request.user.position.name in invite_able_returning():
            return True
        return False
