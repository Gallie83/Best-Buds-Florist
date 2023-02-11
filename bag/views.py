from django.shortcuts import render, redirect
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_bag(request):
    """ Returns shopping bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """Adds item to users bag """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to cart!')

    request.session['bag'] = bag

    return redirect(redirect_url)
