from django.core.management.base import BaseCommand
from myapp_2.models import Client

class Command(BaseCommand):
    help = "Update user name by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')
        parser.add_argument('phone_number', type=str, help='phone number client')
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        phone_number = kwargs.get('phone_number')
        client = Client.objects.filter(pk=pk).first()
        client.phone_number = phone_number
        client.save()
        self.stdout.write(f'{client}')
