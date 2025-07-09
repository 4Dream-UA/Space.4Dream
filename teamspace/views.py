from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

from .models import Project, Team, Worker
from .forms import SearchForm
from config.public_config import invite_able_returning


class AllMembersView(LoginRequiredMixin, ListView):
    model = Worker
    context_object_name = "all_members"
    template_name = "teamspace/all_members.html"
    paginate_by = 7

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super().get_context_data(**kwargs)

        title = self.request.GET.get("title", "")

        context["search_form"] = SearchForm(initial={"title": title})
        return context

    def get_queryset(self):
        queryset = Worker.objects.all()
        title = self.request.GET.get("title")

        if title:
            first, last = (title.split() + [""])[:2]
            return queryset.filter(first_name__icontains=first, last_name__icontains=last)


        return queryset


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
