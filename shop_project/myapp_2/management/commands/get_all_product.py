from django.core.management.base import BaseCommand
from myapp_2.models import Product


class Command(BaseCommand):
    help = "Get all Product"

    def handle(self, *args, **options):
        products = Product.objects.all()
        self.stdout.write(f'{products}')