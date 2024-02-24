from django.urls import path
from .views import products_ordered

urlpatterns = [
    path('client/<int:client_id>/', products_ordered, name='order_client'),
]