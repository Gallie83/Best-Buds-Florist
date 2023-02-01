from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product


def collections(request):
    """ Returns Product type selection page """

    return render(request, 'products/collections.html')


def products(request):
    """ Returns all products page """

    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """ Shows individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)


def product_search(request):
    """ Shows results of user search query """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('home/index.html'))
            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = Product.objects.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)
