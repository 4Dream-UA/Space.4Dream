from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

from config.public_config import priority_returning


class Position(models.Model):
    name = models.CharField(max_length=255)
    rank = models.CharField(
        max_length=63,
        null=True,
        blank=True,
        default="Employee"
    )

    def __str__(self):
        return f"{self.rank} {self.name}"


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    position_priority = models.PositiveSmallIntegerField(default=99)

    def save(self, *args, **kwargs):
        priority = priority_returning()
        if self.position.rank != "Employee":
            self.position_priority = priority.get(f"{self.position.rank} {self.position.name}", 99)
        else:
            self.position_priority = priority.get(self.position.name, 99)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"({self.position.name}) {self.first_name} {self.last_name}"

    class Meta:
        ordering = ["position_priority", "last_name"]


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):

    class Status(models.TextChoices):
        TODO = 'todo', 'To Do'
        IN_PROGRESS = 'in_progress', 'In Progress'
        DONE = 'done', 'Done'

    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=63,
        choices=Status.choices, # noqa -> PyCharm can light it as issue, actually is OK
        default=Status.TODO,
    )
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="assigned_tasks")
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True, blank=True,
        default=None,
        related_name="created_tasks",
    )
    project = models.ForeignKey("Project", on_delete=models.CASCADE, null=True, blank=True, default=None)

    def __str__(self):
        return f"({self.task_type.name}) {self.name}"


class Team(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    workers = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name


class Document(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    document = models.FileField(upload_to="documents/")
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    teams = models.ManyToManyField(Team)
    doc_hub = models.ForeignKey(Document, on_delete=models.CASCADE, null=True, blank=True)
