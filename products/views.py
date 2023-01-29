from django.shortcuts import render

# Create your views here.


def products(request):
    """ Returns Product selection page """

    return render(request, 'products/products.html')
