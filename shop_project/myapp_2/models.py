from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    registration_date = models.DateField()

    def __str__(self):
        return f'Name {self.name}, E-mail {self.email}, Phone {self.phone_number}, Adr. {self.address}, ' \
               f'Date reg. {self.registration_date}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    date_added = models.DateField()

    def __str__(self):
        return f'Name product {self.name}, description {self.description}, Price {self.price}, quantity {self.quantity}, ' \
               f'Date reg. {self.date_added}'

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField()

    def __str__(self):
        return f'Client {self.client}, products {self.products}, total {self.total_amount},date order {self.order_date}'