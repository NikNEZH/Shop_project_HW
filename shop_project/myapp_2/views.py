import logging

from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, Product, Order
from datetime import datetime, timedelta

from .forms import ProductForm
from django.core.files.storage import FileSystemStorage


logger = logging.getLogger(__name__)

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


def add_or_edit_product(request, product_id=1):
    if product_id:
        product = Product.objects.get(pk=product_id)
    else:
        product = Product()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            name = form.cleaned_data['name']
            form.save()
            # photo = form.cleaned_data['photo']
            # fs = FileSystemStorage()
            # fs.save(photo)
            logger.info(f'Получили{name=}')
    else:
        form = ProductForm(instance=product)

    return render(request, 'myapp_2/add_or_edit_product.html', {'form': form})