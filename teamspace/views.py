from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import QuerySet
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from .models import Project, Team, Worker, Task
from .forms import SearchForm
from config.public_config import invite_able_returning


###############################################################
# MEMBER VIEW
###############################################################

class AllMembersView(LoginRequiredMixin, ListView):
    model = Worker
    context_object_name = "all_members"
    template_name = "teamspace/members/all_members.html"
    paginate_by = 7

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:

        context = super().get_context_data(**kwargs)

        title = self.request.GET.get("title", "")

        context["search_form"] = SearchForm(initial={"title": title})
        return context

    def get_queryset(self) -> QuerySet:
        queryset = Worker.objects.select_related("position")
        title = self.request.GET.get("title")

        if title:
            first, last = (title.split() + [""])[:2]
            return queryset.filter(first_name__icontains=first, last_name__icontains=last)


        return queryset


class EditMembersView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Worker
    context_object_name = "member"
    template_name = "teamspace/members/update_member.html"
    fields = [
        "username", "email",
        "first_name", "last_name",
        "avatar", "position_priority",
        "position",
    ]
    success_url = reverse_lazy("teamspace:all_members")

    def test_func(self) -> bool:
        if (self.request.user.position.name in invite_able_returning()
                and self.request.user.position_priority < self.get_object().position_priority):
            return True
        return False


class DeleteMembersView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Worker
    context_object_name = "member"
    template_name = "teamspace/members/delete_member.html"
    success_url = reverse_lazy("teamspace:all_members")

    def test_func(self) -> bool:
        if (self.request.user.position.name in invite_able_returning()
                and self.request.user.position_priority < self.get_object().position_priority):
            return True
        return False


###############################################################
# PROJECT VIEW
###############################################################

# ---> General-Project Views
class CreateProjectView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = "teamspace/projects/create_project.html"
    fields = ["name", "description", "teams"]
    success_url = reverse_lazy("teamspace:all_members")

    def test_func(self) -> bool:
        if self.request.user.position.name in invite_able_returning():
            return True
        return False


class ListProjectView(LoginRequiredMixin, ListView):
    model = Project
    context_object_name = "projects"
    template_name = "teamspace/projects/projects_list.html"
    form_class = SearchForm

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:

        context = super().get_context_data(**kwargs)

        title = self.request.GET.get("title", "")

        context["search_form"] = SearchForm(initial={"title": title})
        return context

    def get_queryset(self) -> QuerySet:
        queryset = Project.objects.prefetch_related("teams")
        title = self.request.GET.get("title")

        if title:
            return queryset.filter(name__icontains=title)


        return queryset


class UpdateProjectView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    context_object_name = "project"
    template_name = "teamspace/projects/update_project.html"
    fields = ["name", "description", "teams"]
    success_url = reverse_lazy("teamspace:project_list")

    def test_func(self) -> bool:
        if self.request.user.position.name in invite_able_returning():
            return True
        return False


class DeleteProjectView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    context_object_name = "project"
    template_name = "teamspace/projects/delete_project.html"
    success_url = reverse_lazy("teamspace:project_list")

    def test_func(self) -> bool:
        if self.request.user.position.name in invite_able_returning():
            return True
        return False

# ---> Member-Project Views
class MemberProjectView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Project
    context_object_name = "project"
    template_name = "teamspace/projects/members_in_project.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.get_object()
        workers = Worker.objects.filter(team__in=project.teams.all()).distinct()
        context["members"] = workers
        return context

    def test_func(self):
        if (
            self.get_object()
            in Project.objects.filter(teams__in=self.request.user.team_set.all()).distinct()
        ):
            return True
        return False

# ---> Task-Project Views
class TaskProjectView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Project
    context_object_name = "project"
    template_name = "teamspace/projects/task_in_project.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.get_object()
        context["tasks"] = Task.objects.filter(
            assignees__team__in=project.teams.all()
        ).distinct()
        return context

    def test_func(self):
        project = self.get_object()
        return project.teams.filter(id__in=self.request.user.team_set.values("id")).exists()


###############################################################
# TEAM VIEW
###############################################################

class ListTeamView(LoginRequiredMixin, ListView):
    model = Team
    context_object_name = "teams"
    template_name = "teamspace/teams/teams_list.html"
    form_class = SearchForm
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:

        context = super().get_context_data(**kwargs)

        title = self.request.GET.get("title", "")

        context["search_form"] = SearchForm(initial={"title": title})
        return context

    def get_queryset(self) -> QuerySet:
        queryset = Team.objects.prefetch_related("workers__position")
        title = self.request.GET.get("title")

        if title:
            return queryset.filter(name__icontains=title)


        return queryset


class CreateTeamView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Team
    template_name = "teamspace/teams/create_team.html"
    fields = '__all__'
    success_url = reverse_lazy("teamspace:teams_list")

    def test_func(self) -> bool:
        if self.request.user.position.name in invite_able_returning():
            return True
        return False


class EditTeamView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Team
    context_object_name = "team"
    template_name = "teamspace/teams/update_team.html"
    fields = '__all__'
    success_url = reverse_lazy("teamspace:teams_list")

    def test_func(self) -> bool:
        if self.request.user.position.name in invite_able_returning():
            return True
        return False


class DeleteTeamView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Team
    context_object_name = "team"
    template_name = "teamspace/teams/delete_team.html"
    fields = '__all__'
    success_url = reverse_lazy("teamspace:teams_list")

    def test_func(self) -> bool:
        if self.request.user.position.name in invite_able_returning():
            return True
        return False
