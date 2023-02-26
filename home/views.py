from django.shortcuts import render
from products.models import Product


# Create your views here.


def index(request):
    """ Returns index.html """

    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'home/index.html', context)


def occasions(request):
    """ Returns occasions.html """

    return render(request, 'home/occasions.html')


def funerals(request):
    """ Returns funerals.html """

    return render(request, 'home/funerals.html')
