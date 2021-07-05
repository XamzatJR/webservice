from django.core.management.base import BaseCommand
from apps.projects.models import Project


class Command(BaseCommand):
    def handle(self, *args, **options):
        query = Project.objects.filter()
        for project in query:
            project.date = project.created_at.date()
            project.save()
