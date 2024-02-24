from django.shortcuts import render, get_object_or_404
from .models import Client, Product, Order
from datetime import datetime, timedelta


def products_ordered(request, client_id):
    today = datetime.now().date()
    last_week = today - timedelta(days=7)
    last_month = today - timedelta(days=30)
    last_year = today - timedelta(days=365)

    client = get_object_or_404(Client, pk=client_id)

    # Получаем все заказы клиента за последние 7 дней и выбираем уникальные товары
    orders_last_week = Order.objects.filter(client=client, order_date__range=[last_week, today])
    products_last_week = Product.objects.filter(order__in=orders_last_week).distinct()

    # Получаем все заказы клиента за последние 30 дней и выбираем уникальные товары
    orders_last_month = Order.objects.filter(client=client, order_date__range=[last_month, today])
    products_last_month = Product.objects.filter(order__in=orders_last_month).distinct()

    # Получаем все заказы клиента за последние 365 дней и выбираем уникальные товары
    orders_last_year = Order.objects.filter(client=client, order_date__range=[last_year, today])
    products_last_year = Product.objects.filter(order__in=orders_last_year).distinct()

    context = {
        'products_last_week': products_last_week,
        'products_last_month': products_last_month,
        'products_last_year': products_last_year
    }

    return render(request, 'myapp_2/order_client.html', context)