from django.core.management.base import BaseCommand
from myapp_2.models import Order


class Command(BaseCommand):
    def handle(self, *args, **options):
        orders = Order.objects.all()

        for order in orders:
            self.stdout.write(f"Заказ №{order.id}:")
            self.stdout.write(f"Клиент: {order.client_id}")
            if order.products.exists():
                products = ", ".join([product.name for product in order.products.all()])
                self.stdout.write(f"Продукт(ы): {products}")
            else:
                self.stdout.write("Продукт: -")
            self.stdout.write(f"Сумма заказа: {order.total_amount:.2f}")
            self.stdout.write(f"Дата оформления: {order.order_date}")