from django.core.management.base import BaseCommand
from myapp_2.models import Client
from faker import Faker
import random
import string

fake = Faker()
class Command(BaseCommand):
    help = 'Creat new client'

    def handle(self, *args, **options):
        # Create random clients
        clients_data = []
        for _ in range(5):
            name = fake.name()
            email = fake.email()
            phone = fake.phone_number()
            address = fake.address()
            registration_date = fake.date_time_this_decade()
            client_data = {'name': name, 'email': email, 'phone_number': phone, 'address': address,
                           'registration_date': registration_date}
            clients_data.append(client_data)
            Client.objects.create(**client_data)
