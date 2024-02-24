from django.core.management.base import BaseCommand
from myapp_2.models import Client


class Command(BaseCommand):
    help = "Get all Client"

    def handle(self, *args, **options):
        clients = Client.objects.all()
        self.stdout.write(f'{clients}')