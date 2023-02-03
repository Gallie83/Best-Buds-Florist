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
    query = None

    if request.GET:
        # Sorting type
        if 'type' in request.GET:
            typeSet = request.GET['type']
            products = products.filter(type=typeSet)

        # Sorting functionality
        if 'sort' in request.GET:
            sortKey = request.GET['sort']
            sort = sortKey
            if sortKey == 'name':
                sortKey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

        # Sorting direction
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortKey = f'-{sortKey}'
            products = products.order_by(sortKey)

        # Searching functionality
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('home/index.html'))
            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = Product.objects.filter(queries)

    current_sort = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_sorting': current_sort,
    }

    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """ Shows individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)
