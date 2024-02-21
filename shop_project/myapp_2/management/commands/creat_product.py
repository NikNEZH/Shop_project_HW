from django.core.management.base import BaseCommand
from myapp_2.models import Product
import random
from faker import Faker


class Command(BaseCommand):
    def handle(self, *args, **options):
        fake = Faker()

        name = input("введите название продукта")
        description = fake.text()
        price = round(random.uniform(1, 1000), 2)
        quantity = random.randint(1, 100)
        date_added = fake.date(pattern="%Y-%m-%d")

        product = Product.objects.create(name=name, description=description, price=price, quantity=quantity,
                                         date_added=date_added)
        self.stdout.write(self.style.SUCCESS(f"Товар №{product.id} успешно добавлен"))