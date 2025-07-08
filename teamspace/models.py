from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


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

    def __str__(self):
        return f"({self.position.name}) {self.first_name} {self.last_name}"


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
        choices=Status.choices,
        default=Status.TODO,
    )
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(settings.AUTH_USER_MODEL)


class Team(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    workers = models.ManyToManyField(settings.AUTH_USER_MODEL)


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    teems = models.ManyToManyField(Team)
