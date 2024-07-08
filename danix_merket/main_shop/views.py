from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from .models import Product, Category


def index(request):
    products = Product.objects.order_by('-created')
    return render(request, 'shop.html', {'data': products})


def single(request, product_id):
    products = get_object_or_404(Product, pk=product_id)
    return render(request, 'single.html', {'product': products})
