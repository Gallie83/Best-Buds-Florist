from django.shortcuts import render
from .models import Product


def Products(request):
    """ Returns Product selection page """

    return render(request, 'products/products.html')


def Flowers(request):
    """ Returns Bouquet products page """

    product = Product.objects.filter(type='FL')

    context = {
        'product': product
    }

    return render(request, 'products/bouquets.html', context)


def Bouquets(request):
    """ Returns Bouquet products page """

    product = Product.objects.filter(type='BQ')

    context = {
        'product': product
    }

    return render(request, 'products/bouquets.html', context)
