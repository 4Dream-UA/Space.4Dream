from django.views.generic import CreateView, ListView

from .models import Project, Team


class AllMembersView(ListView):
    model = Team
    context_object_name = "all_members"
    template_name = "teamspace/all_members.html"


class CreateProjectView(CreateView):
    model = Project
    ...


class CreateTeamView(CreateView):
    model = Team
    fields = '__all__'
    template_name = ""