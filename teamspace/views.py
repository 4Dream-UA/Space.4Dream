from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import QuerySet
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Project, Team, Worker
from .forms import SearchForm
from config.public_config import invite_able_returning



class AllMembersView(LoginRequiredMixin, ListView):
    model = Worker
    context_object_name = "all_members"
    template_name = "teamspace/all_members.html"
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
    template_name = "teamspace/update_member.html"
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
    template_name = "teamspace/delete_member.html"
    success_url = reverse_lazy("teamspace:all_members")

    def test_func(self) -> bool:
        if (self.request.user.position.name in invite_able_returning()
                and self.request.user.position_priority < self.get_object().position_priority):
            return True
        return False


class CreateProjectView(LoginRequiredMixin, CreateView):
    model = Project
    ...


class ListTeamView(LoginRequiredMixin, ListView):
    model = Team
    context_object_name = "teams"
    template_name = "teamspace/teams_list.html"
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
    fields = '__all__'
    template_name = "teamspace/create_team.html"
    success_url = reverse_lazy("teamspace:all_members")

    def test_func(self) -> bool:
        if self.request.user.position.name in invite_able_returning():
            return True
        return False


class EditTeamView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Team
    fields = '__all__'
    context_object_name = "team"
    template_name = "teamspace/update_team.html"
    success_url = reverse_lazy("teamspace:teams_list")

    def test_func(self) -> bool:
        if self.request.user.position.name in invite_able_returning():
            return True
        return False
