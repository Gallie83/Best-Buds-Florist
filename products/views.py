from django.shortcuts import render
from .models import Product


def products(request):
    """ Returns Product selection page """

    return render(request, 'products/products.html')


def bouquets(request):
    """ Returns Bouquet products page """

    product = Product.objects.filter(type='BQ')

    context = {
        'product': product
    }

    return render(request, 'products/bouquets.html', context)
