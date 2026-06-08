from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from teamspace.models import ActionLog, SystemSetting

class Command(BaseCommand):
    """
    docker-compose exec web python manage.py clean_logs
    """
    help = 'Deletes logs older than the retention period specified in SystemSettings'

    def handle(self, *args, **kwargs):
        settings = SystemSetting.objects.first()
        if not settings:
            self.stdout.write(self.style.WARNING("System settings not found. Aborting cleanup."))
            return

        days = settings.log_retention_days
        cutoff_date = timezone.now() - timedelta(days=days)

        old_logs = ActionLog.objects.filter(timestamp__lt=cutoff_date)
        count = old_logs.count()
        old_logs.delete()

        self.stdout.write(self.style.SUCCESS(f"Successfully deleted {count} old logs (older than {days} days)."))