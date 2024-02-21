from django.core.management.base import BaseCommand
from myapp_2.models import Order, Client, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        client_id = input("Введите ID клиента, сделавшего заказ: ")
        total_amount = float(input("Введите общую сумму заказа: "))
        date = input("Введите дату оформления заказа (в формате ГГГГ-ММ-ДД): ")

        if not client_id.isdigit():
            self.stdout.write(self.style.ERROR("ID клиента должен быть числом"))
            return

        if not Client.objects.filter(id=client_id).exists():
            self.stdout.write(self.style.ERROR("Клиента с таким ID не существует"))
            return

        product_id = input("Введите ID товара: ")
        if not product_id.isdigit():
            self.stdout.write(self.style.ERROR("ID товара должен быть числом"))
            return

        if not Product.objects.filter(id=product_id).exists():
            self.stdout.write(self.style.ERROR("Товара с таким ID не существует"))
            return

        product = Product.objects.get(id=product_id)

        order = Order.objects.create(client_id=client_id, total_amount=total_amount, order_date=date)
        order.products.add(product)

        self.stdout.write(self.style.SUCCESS(f"Заказ №{order.id} успешно добавлен"))