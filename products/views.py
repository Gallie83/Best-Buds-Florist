from django.shortcuts import render
from .models import Product


def products(request):
    """ Returns Product selection page """

    return render(request, 'products/products.html')


def flowers(request):
    """ Returns Bouquet products page """

    product = Product.objects.filter(type='FL')

    context = {
        'product': product
    }

    return render(request, 'products/flowers.html', context)


def bouquets(request):
    """ Returns Bouquet products page """

    product = Product.objects.filter(type='BQ')

    context = {
        'product': product
    }

    return render(request, 'products/bouquets.html', context)


def indoor_plants(request):
    """ Returns Bouquet products page """

    product = Product.objects.filter(type='IP')

    context = {
        'product': product
    }

    return render(request, 'products/indoor_plants.html', context)
