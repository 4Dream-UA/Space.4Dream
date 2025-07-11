from django import template

register = template.Library()

@register.filter
def unique_projects(teams):
    seen = set()
    unique = []
    for team in teams:
        for project in team.project_set.all():
            if project.id not in seen:
                seen.add(project.id)
                unique.append(project)
    return unique