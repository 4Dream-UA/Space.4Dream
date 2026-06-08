from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.core.exceptions import ValidationError
from django.utils.html import format_html

from .models import Position, Worker, TaskType, Task, Team, Project, Document


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ["name", "rank"]
    list_filter = ["name", "rank"]
    search_fields = ["name"]


class WorkerChangeForm(UserChangeForm):
    class Meta:
        model = Worker
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        role = cleaned_data.get('role')
        is_active = cleaned_data.get('is_active')

        if self.instance.pk and self.instance.role == Worker.Role.ADMIN:
            if role != Worker.Role.ADMIN or not is_active:
                admin_count = Worker.objects.filter(
                    role=Worker.Role.ADMIN,
                    is_active=True
                ).exclude(pk=self.instance.pk).count()

                if admin_count == 0:
                    raise ValidationError(
                        "Critical error: You cannot revoke permissions or deactivate "
                        "the last active administrator in the system!"
                    )
        return cleaned_data


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    form = WorkerChangeForm

    list_display = (
        "username",
        "get_full_name",
        "role_badge",
        "position",
        "is_active",
    )

    list_filter = ("role", "position", "is_active", "is_staff")

    search_fields = ("username", "first_name", "last_name", "email", "telegram")

    fieldsets = (
        ("Login", {
            "fields": ("username", "password")
        }),
        ("Personal information", {
            "fields": ("first_name", "last_name", "email", "age", "avatar")
        }),
        ("Operational data", {
            "fields": ("role", "position")
        }),
        ("Contact Information and SM", {
            "fields": ("telegram", "skype", "linkedin_url", "github_url"),
            "classes": ("collapse",)
        }),
        ("System privileges (Advanced)", {
            "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions"),
            "classes": ("collapse",)
        }),
        ("Dates", {
            "fields": ("last_login", "date_joined"),
            "classes": ("collapse",)
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Personal information", {
            "fields": ("first_name", "last_name", "email")
        }),
        ("Operational data", {
            "fields": ("role", "position")
        }),
    )

    @admin.display(description="Role")
    def role_badge(self, obj):
        colors = {
            Worker.Role.ADMIN: 'red',
            Worker.Role.MANAGER: '#f59e0b',
            Worker.Role.USER: 'green',
        }
        color = colors.get(obj.role, 'gray')
        return format_html(
            '<span style="color: {}; font-weight: bold; padding: 4px 8px; border: 1px solid {}; border-radius: 4px;">{}</span>',
            color, color, obj.get_role_display()
        )

    def delete_model(self, request, obj):
        if obj.role == Worker.Role.ADMIN:
            admin_count = Worker.objects.filter(role=Worker.Role.ADMIN, is_active=True).count()
            if admin_count <= 1:
                messages.error(request, "Security error: The last administrator cannot be deleted!")
                return
        super().delete_model(request, obj)

    def delete_queryset(self, request, queryset):
        admins_to_delete = queryset.filter(role=Worker.Role.ADMIN)
        if admins_to_delete.exists():
            total_admins = Worker.objects.filter(role=Worker.Role.ADMIN, is_active=True).count()
            if total_admins - admins_to_delete.count() < 1:
                messages.error(request, "Security warning: This action will remove all administrators. Operation canceled.")
                return
        super().delete_queryset(request, queryset)


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["name", "task_type", "priority", "is_completed", "deadline", "project", "created_by"]
    list_filter = ["is_completed", "priority", "task_type", "project", "deadline"]
    search_fields = ["name", "description"]
    filter_horizontal = ["assignees"]
    date_hierarchy = "deadline"


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    search_fields = ["name", "description"]
    filter_horizontal = ["workers"]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    search_fields = ["name", "description"]
    filter_horizontal = ["teams"]


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ["name", "worker", "project", "date"]
    list_filter = ["date", "project", "worker"]
    search_fields = ["name", "description"]
    date_hierarchy = "date"