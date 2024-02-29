from django.contrib import admin
from .models import Client, Product, Order


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number',]


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['get_client_name', 'get_products_list', 'total_amount', 'order_date']

    def get_products_list(self, obj):
        return ", ".join([product.name for product in obj.products.all()])
    get_products_list.short_description = 'Продукция'

    def get_client_name(self, obj):
        return obj.client.name
    get_client_name.short_description = 'Имя клиента'


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
