from django.urls import path
from .views import products_ordered, add_or_edit_product

urlpatterns = [
    path('client/<int:client_id>/', products_ordered, name='order_client'),
    path('product/<int:product_id>/', add_or_edit_product, name='edit_product'),
]