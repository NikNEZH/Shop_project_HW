from django.shortcuts import render
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)
# Create your views here.


def main(request):
    logger.info(f'Info page {object.__name__} accessed')
    return render(request, 'shop/main.html')


def about_us(request):
    logger.info(f'Info page {object.__name__} accessed')
    return render(request, 'shop/about_us.html')