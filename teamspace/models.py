from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class Position(models.Model):
    name = models.CharField(max_length=255)
    rank = models.CharField(max_length=63, null=True, blank=True, default="Employee")

    def __str__(self):
        return f"{self.rank} {self.name}"


class Worker(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "admin", "Admin"
        MANAGER = "manager", "Manager"
        USER = "user", "User"

    role = models.CharField(
        max_length=20, choices=Role.choices, default=Role.USER, verbose_name="Role"
    )
    age = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Age")

    linkedin_url = models.URLField(
        max_length=255, null=True, blank=True, verbose_name="LinkedIn"
    )
    github_url = models.URLField(
        max_length=255, null=True, blank=True, verbose_name="GitHub"
    )
    skype = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Skype"
    )
    telegram = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Telegram"
    )

    position = models.ForeignKey(
        "Position", on_delete=models.CASCADE, null=True, blank=True
    )
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    position_priority = models.PositiveSmallIntegerField(default=99)

    def save(self, *args, **kwargs):
        role_priorities = {
            self.Role.ADMIN: 1,
            self.Role.MANAGER: 2,
            self.Role.USER: 3,
        }

        self.position_priority = role_priorities.get(self.role, 3)

        super().save(*args, **kwargs)

    def __str__(self):
        pos_name = (
            self.position.name
            if hasattr(self, "position") and self.position
            else "No Position"
        )
        full_name = f"{self.first_name} {self.last_name}".strip()
        display_name = full_name if full_name else self.username

        return f"[{self.get_role_display()}] ({pos_name}) {display_name}"

    class Meta:
        ordering = ["position_priority", "last_name"]


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    class Status(models.TextChoices):
        TODO = "todo", "To Do"
        IN_PROGRESS = "in_progress", "In Progress"
        DONE = "done", "Done"

    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=63,
        choices=Status.choices,  # noqa -> PyCharm can light it as issue, actually is OK
        default=Status.TODO,
    )
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="assigned_tasks"
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
        related_name="created_tasks",
    )
    project = models.ForeignKey(
        "Project", on_delete=models.CASCADE, null=True, blank=True, default=None
    )

    class Meta:
        ordering = ["is_completed"]

    def __str__(self):
        return f"({self.task_type.name}) {self.name}"


class Team(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    workers = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    teams = models.ManyToManyField(Team)

    def __str__(self):
        return self.name


class Document(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    document = models.FileField(upload_to="documents/")
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="documents",
    )
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["date"]


class SystemSetting(models.Model):
    log_retention_days = models.PositiveIntegerField(
        default=30, verbose_name="How many days to keep logs"
    )

    class Meta:
        verbose_name = "System Setting"
        verbose_name_plural = "System Settings"

    def save(self, *args, **kwargs):
        if not self.pk and SystemSetting.objects.exists():
            return
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Settings (Keep logs for {self.log_retention_days} days)"


class ActionLog(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True
    )
    method = models.CharField(max_length=10)
    path = models.CharField(max_length=255)
    status_code = models.PositiveIntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timestamp"]
        verbose_name = "User Action Log"
        verbose_name_plural = "User Action Logs"

    def __str__(self):
        username = self.user.username if self.user else "Anonymous"
        return f"[{self.timestamp.strftime('%Y-%m-%d %H:%M')}] {username} -> {self.method} {self.path}"
