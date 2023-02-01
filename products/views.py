from django.shortcuts import render, get_object_or_404
from .models import Product


def products(request):
    """ Returns Product type selection page """

    return render(request, 'products/products.html')


def specials(request):
    """ Returns Specials products page """

    products = Product.objects.filter(type='SP')

    context = {
        'products': products
    }

    return render(request, 'products/specials.html', context)


def bouquets(request):
    """ Returns Bouquet products page """

    products = Product.objects.filter(type='BQ')

    context = {
        'products': products
    }

    return render(request, 'products/bouquets.html', context)


def indoor_plants(request):
    """ Returns Indoor Plants page """

    products = Product.objects.filter(type='IP')

    context = {
        'products': products
    }

    return render(request, 'products/indoor_plants.html', context)


def product_details(request, product_id):
    """ Shows individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)
