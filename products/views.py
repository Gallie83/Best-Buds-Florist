from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models.functions import Lower
from django.contrib import messages
from django.db.models import Q
from .models import Product


def collections(request):
    """ Returns Product type selection page """

    return render(request, 'products/collections.html')


def products(request):
    """ Returns all products page, including sorting """

    products = Product.objects.all()

    sort = None
    direction = None

    if 'sort' in request.GET:
        sortKey = request.GET['sort']
        sort = sortKey
        if sortKey == 'name':
            sortKey = 'lower_name'
            products = products.annotate(lower_name=Lower('name'))

        if 'direction' in request.GET:
            direction = request.GET['direction']
            if direction == 'desc':
                sortKey = f'-{sortKey}'
        products = products.order_by(sortKey)

    context = {
        'products': products
    }

    return render(request, 'products/products.html', context)


def bouquets(request):
    """ Returns page with only bouquets """

    products = Product.objects.filter(type='BQ')

    sort = None
    direction = None

    if 'sort' in request.GET:
        sortKey = request.GET['sort']
        sort = sortKey
        if sortKey == 'name':
            sortKey = 'lower_name'
            products = products.annotate(lower_name=Lower('name'))

        if 'direction' in request.GET:
            direction = request.GET['direction']
            if direction == 'desc':
                sortKey = f'-{sortKey}'
        products = products.order_by(sortKey)

    context = {
        'products': products
    }

    return render(request, 'products/products.html', context)


def specials(request):
    """ Returns page with only specials """

    products = Product.objects.filter(type='SP')

    context = {
        'products': products
    }

    return render(request, 'products/products.html', context)


def indoor_plants(request):
    """ Returns page with only indoor plants """

    products = Product.objects.filter(type='IP')

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
